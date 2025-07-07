from django.contrib.auth.models import Group
from django.contrib import messages
from django.urls import reverse
from django.views.generic import DeleteView


class DelGrupos(DeleteView):
    model = Group
    
    def get_success_url(self):
        return reverse('listagem_grupos')

    def form_invalid(self, form):
        messages.error(self.request, "Erro na Deleção do Grupo. {}".format(form.errors))
        return super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, "Grupo Deletado com sucesso")
        return super().form_valid(form)
    
    