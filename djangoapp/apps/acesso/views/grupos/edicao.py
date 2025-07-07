import re
from django.contrib.auth.models import Permission, Group
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.views.generic import UpdateView

from apps.acesso.forms import GroupForm


class EdiGrupos(UpdateView):
    template_name='acesso/grupos/edicao.html'
    form_class = GroupForm
    model = Group
    
    def get_success_url(self):
        return reverse('listagem_grupos')
    
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
        groups_permissions_list = ",".join([str(x) for x in self.object.permissions.all().values_list('id',flat=True)])
        context['group_permissions'] = "({})".format(groups_permissions_list)
        context['permissions'] = Permission.objects.filter().exclude(content_type_id__in=[1,5,6,8,9])        

        return context
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro na Edição do Grupo. {}".format(form.errors))
        return super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, "Grupo salvo com sucesso")
        return super().form_valid(form)
    
    