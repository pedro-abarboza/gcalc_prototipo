from django.conf import settings
from django.contrib import messages
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from apps.utils.celery.base import CeleryTaskMixin
from apps.calculos.tasks import import_pjecalc_task
# Create your views here.


class UploadPjeCalc(TemplateView, CeleryTaskMixin):

    template_name='calculos/upload_pjecalc.html'
    task_result = None
        
        
    def get_url_return(self):
        return reverse('pjecalc_upload')
       
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Cálculo',
                'url': '',
                'activate': None
            },{
                'title': 'Upload - PJE-Calc',
                'url': '',
                'activate': 'true'
            }
        ]
        context['title'] = 'Upload'
        context['card_title'] = 'PJE-Calc'
        context['subtitle'] = 'Aqui você faz o upload de arquivos em PDF, originados do PJE-Calc, que teram os valores do resumo salvos no banco de dados.'
        
        return context
    
    def salvar_temporarios(self, file):
        # Salve o arquivo temporariamente
        nome_arq = '{}/tmp/{}'.format(
            settings.MEDIA_ROOT,
            file.name
        )
        with default_storage.open(nome_arq, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return destination.name
    
    def post(self, request, *args, **kwargs):
        files = self.request.FILES.getlist('arquivo')
        temporarios = []
        for file in files:
            nome_arq = self.salvar_temporarios(file)
            temporarios.append(nome_arq)

        self.task_result = import_pjecalc_task.apply_async(
            kwargs={'dados':temporarios}
        )

        return render(self.request, self.progressbar_template_name, self.set_task_params)

