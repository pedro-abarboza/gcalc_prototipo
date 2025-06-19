from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse
from django.views.generic import DeleteView
from django.contrib import messages

from apps.processos.models import Processos


class DelProcessos(DeleteView):
    model = Processos
    
    def get_success_url(self):
        return reverse('listagem_processos')

    def form_invalid(self, form):
        messages.error(self.request, "Erro na Deleção do Processo. {}".format(form.errors))
        return super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, "Processo Deletado com sucesso")
        return super().form_valid(form)
    
    