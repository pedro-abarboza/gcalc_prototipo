import re
import camelot

from datetime import datetime

from PyPDF2 import PdfReader
from apps.calculos.models import Calculos, VerbasCalc, \
    DebitosReclamado, CredDesReclamante, VerbasCalcDetalhes
from apps.processos.models import Reclamantes, Reclamadas, \
    Processos
from core.celery import app as celery_app
from celery_progress.backend import ProgressRecorder


def get_number(item):
    #verifica se o numero é negativo
    negativo = False
    if '(' in item:
        negativo = True

    #retira strings
    numero = re.findall(r'[\d\.,]+',item)
    if numero:
        numero = numero[0]
    else:
        return None

    #verifica se é um digito
    if numero.replace('.','').replace(',','').isdigit():
        #formata o numero para salvar
        numero = numero.replace('.','').replace(',','.')
    else:
        None

    return '-'+numero if negativo else numero


@celery_app.task(bind=True, name='task.import_pjecalc')
def import_pjecalc_task(self, **kwargs):
    files = kwargs['dados']
    progress_recorder = ProgressRecorder(self)
    total_progress_recorder = int(len(files)*5)
    progress = 0
    progress_recorder.set_progress(progress, total_progress_recorder, description="Iniciando Importação...")

    for file in files:
        arq_name=file.split('/')[-1]
        pdf_reader = PdfReader(file)
        pg_inicio = 0

        progress+=1
        progress_recorder.set_progress(progress, total_progress_recorder, 
            description="Lendo arquivo PJE-Calc - {}...".format(arq_name))

        #unir paginas
        all_pages = ''
        for pagina in pdf_reader.pages:
            all_pages+= pagina.extract_text()

        #separar linhas
        all_pages = all_pages.split('\n')

        progress+=1
        progress_recorder.set_progress(progress, total_progress_recorder, 
            description="Buscando dados do Processo - {}...".format(arq_name))
        
        #Salva Reclamada
        reclamada = all_pages[4].replace(' '.join(all_pages[4].split(' ')[:3])[:23], '')
        reclamada, reclamada_create = Reclamadas.objects.get_or_create(nome=reclamada)
        #Salva Reclamante
        reclamante = all_pages[5].replace(all_pages[5].split(' ')[0][:10], '')
        reclamante, reclamante_create = Reclamantes.objects.get_or_create(nome=reclamante)
        dados_calculo = {}

        #pegar dados do processo
        dados_processo = {
            'n_processo': all_pages[0],
            'reclamada': reclamada,
            'reclamante': reclamante,
            'dt_ajuizamento': datetime.strptime(all_pages[7].split(' ')[0], '%d/%m/%Y')
        }

        #Salva os dados do processo
        processo, processo_create = Processos.objects.get_or_create(**dados_processo)

        progress+=1
        progress_recorder.set_progress(progress, total_progress_recorder, 
            description="Buscando dados do Cálculo - {}...".format(arq_name))

        #pegar dados do Calculo
        dados_calculo = {
            'processo': processo,
            'dt_inicio_calc': datetime.strptime(all_pages[4].split(' ')[0], '%d/%m/%Y'),
            'dt_fim_calc': datetime.strptime(all_pages[4].split(' ')[2][:10], '%d/%m/%Y'),
            'dt_liquidacao': datetime.strptime(all_pages[5].split(' ')[0][:10], '%d/%m/%Y'),
            'n_arquivo': arq_name,
            'n_pje': all_pages[1].replace('Processo:','').split(' ')[1]
        }

        for item in all_pages:
            if 'Percentual de Parcelas Remuneratórias e Tributáveis' in item:
                dados_calculo['per_parcelas_rt'] = item.split()[-1].replace("%", '').replace(',','.')
                break

        calculo = Calculos.objects.create(**dados_calculo)
        
        progress+=1
        progress_recorder.set_progress(progress, total_progress_recorder, 
            description="Buscando Valores do Resumo - {}...".format(arq_name))
        
        tabelas = camelot.read_pdf(file, pages = str(pg_inicio)+'-2', )
        verbas = []
        for tabela in tabelas:
            if tabela.df[0][0] == 'Descrição do Bruto Devido ao Reclamante':
                #entra na tabela de verbas
                for idx in tabela.df[1:].transpose():
                    linha = tabela.df[1:].transpose()[idx]
                    progress_recorder.set_progress(progress, total_progress_recorder, 
                        description="Salvando{} - {}...".format(linha[0], arq_name))
                    verba = VerbasCalc.objects.create(
                        calculo = calculo,
                        descricao = linha[0], 
                        v_corrigido = get_number(linha[1]), 
                        juros = get_number(linha[2]), 
                        total = get_number(linha[3])
                    )
                    verbas.append(verba)

            elif tabela.df[0][0] == 'Descrição de Débitos do Reclamado por Credor':
                #entra na tabela de debitos da Reclamada
                for idx in tabela.df[1:].transpose():
                    linha = tabela.df[1:].transpose()[idx]
                    progress_recorder.set_progress(progress, total_progress_recorder, 
                        description="Salvando{} - {}...".format(linha[0], arq_name))
                    DebitosReclamado(
                        calculo = calculo, 
                        descricao = linha[0], 
                        valor = get_number(linha[1])
                        ).save()

            elif tabela.df[0][0] =='Descrição de Créditos e Descontos do Reclamante':
                #entra na tabela de creditos e descontos do Reclamante
                for idx in tabela.df[1:].transpose():
                    linha = tabela.df[1:].transpose()[idx]
                    progress_recorder.set_progress(progress, total_progress_recorder, 
                        description="Salvando{} - {}...".format(linha[0], arq_name))
                    CredDesReclamante(
                        calculo = calculo,
                        descricao = linha[0], 
                        valor = get_number(linha[1])).save()

        progress+=1
        progress_recorder.set_progress(progress, total_progress_recorder, 
            description="Buscando Demonstrativo de Verbas - {}...".format(arq_name))
        #buscando detalhamento das verbas
        n_linha = 0
        for idx, linha in enumerate(all_pages[n_linha:]):
            if 'Demonstrativo de Verbas' in linha:
                n_linha = idx
                break

        for verba in verbas:
            if verba.descricao == 'Total':
                from django.db.models import Sum
                totais = VerbasCalcDetalhes.objects.filter(verba__calculo = calculo)
                verba.v_devido = totais.aggregate(Sum('devido'))['devido__sum']
                verba.v_pago = totais.aggregate(Sum('pago'))['pago__sum']
                verba.v_calculado = totais.aggregate(Sum('diferenca'))['diferenca__sum']
                verba.save()
                break
            progress_recorder.set_progress(progress, total_progress_recorder, 
            description="Detalhes - {} - {}...".format(verba.descricao, arq_name))
            devido = 0
            pago = 0
            diferenca = 0
            for idx, linha in enumerate(all_pages[n_linha:]):
                if verba.descricao in linha:
                    linha_v = all_pages[n_linha+idx]
                    while not 'Total' in linha_v:

                        if linha_v[:2].isdigit() and linha_v[3:4]=='a' \
                            and linha_v[5:7].isdigit() and linha_v[7:8]=='/':
                            valores = linha_v.split(' ')
                            valores = [item for item in valores if item != '']
                            VerbasCalcDetalhes(
                                verba = verba,
                                data = datetime.strptime('01'+valores[2][2:], '%d/%m/%Y'),
                                base = get_number(valores[3]),
                                divisor = get_number(valores[4]),
                                multiplicador = get_number(valores[5]),
                                quantidade = get_number(valores[6]),
                                dobra = True if valores[7]=='Sim' else False,
                                devido = get_number(valores[8]),
                                pago = get_number(valores[9]),
                                diferenca = get_number(valores[10]),
                                icm = get_number(valores[11]),
                                v_corrigido = get_number(valores[12]),
                            ).save()

                            devido += float(get_number(valores[8]))
                            pago += float(get_number(valores[9]))
                            diferenca += float(get_number(valores[10]))
                        
                        n_linha+=1
                        linha_v = all_pages[n_linha]
                    n_linha+=1
                    break

                else:
                    continue
            
            #Somar totais das verbas
            verba.v_devido = devido
            verba.v_pago = pago
            verba.v_calculado = diferenca
            verba.save()
