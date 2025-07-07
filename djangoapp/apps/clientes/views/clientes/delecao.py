import json
from django.db.models.base import Model as Model
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import DeleteView
from django.contrib import messages

from apps.clientes.models import Clientes


class DelClientes(DeleteView):
    template_name='clientes/delecao.html'
    model = Clientes

    def get_success_url(self):
        return reverse('listagem_clientes')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Deleção de Cliente'
        context['object'] = self.get_object()
        return context
    
    def get_object(self, queryset = None):
        if 'pk' not in self.kwargs:
            self.kwargs['pk'] = self.request.POST['id']
        return super().get_object(queryset)

    def form_invalid(self, form):
        messages.error(self.request, "Erro na Deleção do Cliente. {}".format(form.errors))
        return super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, "Cliente Deletado com sucesso")
        return super().form_valid(form)
    
    