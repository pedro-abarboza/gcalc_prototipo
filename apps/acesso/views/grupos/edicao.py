import re
from django.contrib.auth.models import Permission, Group
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.views.generic import UpdateView

from apps.acesso.forms import GroupForm


class EdiGrupos(UpdateView):
    template_name='acesso/grupos/form.html'
    form_class = GroupForm
    model = Group
    
    def get_success_url(self):
        return reverse('listagem_grupos')
    
    def get_url_form(self):
        return reverse('edicao_grupos')
    
    def get_object(self, queryset = None):
        if 'pk' in self.request.POST and self.request.POST['pk']:
            self.kwargs['pk'] = self.request.POST['pk']
        return super().get_object(queryset)
    
    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Acesso',
                'url': None,
                'activate': 'true'
            },{
                'title': 'Grupos',
                'url': None,
                'activate': 'true'
            },{
                'title': 'Edição',
                'url': None,
                'activate': 'true'
            }
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Grupos'
        context['card_title'] = 'Edição'
        context['subtitle'] = 'Aqui você edita os Grupos.'
        context['form'] = self.get_form()
        context['group_permissions'] = list(self.object.permissions.all().values_list('id',flat=True))
        context['permissions'] = Permission.objects.filter().exclude(content_type_id__in=[1,4,5])
        context['url_form'] = self.get_url_form()
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro na Edição do Grupo. {}".format(form.errors))
        return super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, "Grupo salvo com sucesso")
        return super().form_valid(form)
    
    