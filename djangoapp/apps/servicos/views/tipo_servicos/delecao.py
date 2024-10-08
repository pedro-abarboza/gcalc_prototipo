from django.urls import reverse
from django.views.generic import DeleteView
from django.contrib import messages

from apps.servicos.models import TipoServico

class DelTipoServico(DeleteView):
    model = TipoServico
    
    def get_success_url(self):
        return reverse('listagem_tipo_servicos')

    def form_invalid(self, form):
        messages.error(self.request, "Erro na Deleção do Tipo de Servico. {}".format(form.errors))
        response = super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, "Tipo de Servico Deletado com sucesso")
        return super().form_valid(form)
    
    