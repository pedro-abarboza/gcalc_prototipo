import os
from django.conf import settings
from django.http import FileResponse, Http404, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import UpdateView

from apps.sistema.models import Parametros


class SistemaView(UpdateView):
    model = Parametros
    template_name='sistema/sistema.html'
    fields = '__all__'


    def get_breadcrumbs(self):
        return [
            {
                'title': 'Sistema',
                'url': 'sistema',
                'activate': 'true'
            },
        ]
    
    def get_success_url(self):
        return reverse('sistema')
    
    def get_object(self, queryset = None):
        try:
            param = Parametros.objects.latest('id')
        except:
            param = Parametros.objects.get_or_create()[0]
        return param
        
    
    def get_form_class(self):
        form_class = super().get_form_class()
        for item in form_class.base_fields:
            form_class.base_fields[item].widget.attrs['class'] = 'form-control'

        return form_class
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Sistema'
        context['card_title'] = 'Sistema'
        context['subtitle'] = 'Bem vindo ao G-Calc.'
        return context
    
    def form_valid(self, form):
        param = self.get_object()
        if 'logo_icon' in self.request.FILES:
            logo_icon = os.path.join(settings.MEDIA_ROOT,'logo/logo-icon.png')
            if os.path.exists(logo_icon):
                param.logo_icon.delete()
            mime = form.instance.logo_icon.name.split('.')[-1]
            form.instance.logo_icon.name = 'logo-icon.'+mime
        if 'logo_text' in self.request.FILES:
            logo_text = os.path.join(settings.MEDIA_ROOT,'logo/logo-text.png')
            if os.path.exists(logo_text):
                param.logo_text.delete()
            mime = form.instance.logo_text.name.split('.')[-1]
            form.instance.logo_text.name = 'logo-text.'+mime
            
        return super().form_valid(form)

def servir_imagem_logo(request, nome_arquivo):
    caminho_arquivo = os.path.join(settings.MEDIA_ROOT, 'logo', nome_arquivo)
    if not os.path.exists(caminho_arquivo):
        caminho_arquivo = os.path.join(settings.MEDIA_ROOT, 'logo_default', nome_arquivo)
    with open(caminho_arquivo, "rb") as f:
        return HttpResponse(f.read())
