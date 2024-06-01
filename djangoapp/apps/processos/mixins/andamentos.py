

import json
import requests
from datetime import datetime

from apps.processos.models import Andamentos

class AndamentosMixin:

    def get_consulta(self, processo):
        API_KEY = "cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw=="

        LINKS_TRIBUNAIS = [
            "https://api-publica.datajud.cnj.jus.br/api_publica_tst/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt1/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt2/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt3/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt4/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt5/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt6/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt7/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt8/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt9/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt10/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt11/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt12/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt13/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt14/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt15/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt16/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt17/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt18/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt19/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt20/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt21/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt22/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt23/_search",
            "https://api-publica.datajud.cnj.jus.br/api_publica_trt24/_search",
        ]

        numero_processo = processo.n_processo.replace(".",'').replace("-","")
        numero_regiao = int(numero_processo[14:16])
        payload = json.dumps({
            "query": {
                "match": {
                "numeroProcesso": "{}".format(numero_processo)
                }
            }
        })

        #Substituir <API Key> pela Chave Pública
        headers = {
            'Authorization': 'ApiKey {}'.format(API_KEY),
            'Content-Type': 'application/json'
        }

        links = [LINKS_TRIBUNAIS[numero_regiao], LINKS_TRIBUNAIS[0]]
        Andamentos.objects.filter(processo=processo).delete()
        for link in links:
            response = requests.request("POST", link, headers=headers, data=payload)
            response = response.json()['hits']['hits']
            for instancia in response:
                andamentos = instancia['_source']
                grau = instancia['_source']['grau']+' - '+instancia['_source']['classe']['nome']
                data = []
                for mov in andamentos['movimentos']:
                    data.append(
                        Andamentos(
                            processo=processo,
                            descricao=mov['nome'],
                            dt_andamento=datetime.strptime(mov['dataHora'][:10], '%Y-%m-%d'),
                            codigo=mov['codigo'],
                            grau=grau
                        )
                    )
                Andamentos.objects.bulk_create(data, batch_size=100)
        processo.dt_ult_verificacao = datetime.now()
        processo.save()