from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse
from django.views.generic import DeleteView
from django.contrib import messages

from apps.servicos.models import Servicos


class DelServicos(DeleteView):
    template_name='servicos/deletar.html'
    model = Servicos
    
    def get_success_url(self):
        return reverse('listagem_servicos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_title'] = 'Deleção de Serviçoos'
        context['object'] = self.get_object()
        
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Erro na Deleção do Serviço. {}".format(form.errors))
        return super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, "Serviço Deletado com sucesso")
        return super().form_valid(form)
    
    