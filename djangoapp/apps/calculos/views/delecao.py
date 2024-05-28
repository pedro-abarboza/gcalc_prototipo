from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse
from django.views.generic import DeleteView
from django.contrib import messages

from apps.calculos.models import Calculos


class DelCalculos(DeleteView):
    model = Calculos
    
    def get_success_url(self):
        return reverse('listagem_calculos')

    def form_invalid(self, form):
        messages.error(self.request, "Erro na Deleção do Cálculo. {}".format(form.errors))
        response = super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, "Cálculo Deletado com sucesso")
        return super().form_valid(form)