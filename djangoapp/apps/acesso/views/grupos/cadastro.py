from django.urls import reverse
from django.views.generic import CreateView
from django.contrib import messages

from django.contrib.auth.models import Group, Permission
from apps.acesso.forms import GroupForm


class CadGrupos(CreateView):
    template_name='acesso/grupos/cadastro.html'
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
                'url': '',
                'activate': None
            },{
                'title': 'Grupos',
                'url': '',
                'activate': None
            },{
                'title': 'Cadastro',
                'url': '',
                'activate': 'True'
            }
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Grupos'
        context['card_title'] = 'Cadastro'
        context['subtitle'] = 'Aqui você cadastra novos Grupos.'
        context['permissions'] = Permission.objects.filter().exclude(content_type_id__in=[1,5,6,8,9])
        context['form'] = self.get_form()
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro no salvamento do Grupo. {}".format(form.errors))
        return super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, "Grupo salvo com sucesso")
        return super().form_valid(form)
    
    