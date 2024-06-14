from django.db.models.base import Model as Model
from django.urls import reverse
from django.views.generic import DeleteView
from django.contrib import messages

from apps.clientes.models import Clientes


class DelClientes(DeleteView):
    model = Clientes
    
    def get_success_url(self):
        return reverse('listagem_clientes')

    def form_invalid(self, form):
        messages.error(self.request, "Erro na Deleção do Cliente. {}".format(form.errors))
        return super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, "Cliente Deletado com sucesso")
        return super().form_valid(form)
    
    