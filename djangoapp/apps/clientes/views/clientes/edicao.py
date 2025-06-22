from django.urls import reverse
from django.views.generic import UpdateView
from django.contrib import messages

from apps.clientes.models import Clientes


class EdiClientes(UpdateView):
    template_name='clientes/form.html'
    model = Clientes
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('listagem_clientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_title'] = 'Edição de Cliente'
        context['subtitle'] = 'Aqui você edita os dados do {}.'.format(self.object.nome)
        context['subtitle_list'] = 'Aqui visualiza os Tipos de Serviços cadastrados para {}.'.format(self.object.nome)
        context['form'] = self.get_form()
        
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro na Edição do Cliente. {}".format(form.errors))
        return super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, "Cliente salvo com sucesso")
        return super().form_valid(form)
    
    