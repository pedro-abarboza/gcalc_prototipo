from typing import Any
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib import messages

from apps.acesso.views.usuarios.form import CustomUserCreationForm


class CadUsuarios(CreateView):
    template_name='acesso/usuarios/cadastro.html'
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse('listagem_usuarios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Usuarios'
        context['card_title'] = 'Cadastro'
        context['subtitle'] = 'Aqui você cadastra novos Usuarios.'
        context['form'] = self.get_form()
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro no salvamento do Usuário. {}".format(form.errors))
        return HttpResponseRedirect(self.get_success_url())
        
    def form_valid(self, form):
        messages.success(self.request, "Usuário salvo com sucesso")
        return super().form_valid(form)
    
    