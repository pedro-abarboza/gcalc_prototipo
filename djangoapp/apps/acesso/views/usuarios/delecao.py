from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.views.generic import DeleteView


class DelUsuarios(DeleteView):
    model = User
    
    def get_success_url(self):
        return reverse('listagem_usuarios')

    def form_invalid(self, form):
        messages.error(self.request, "Erro na Deleção do Usuario. {}".format(form.errors))
        return super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, "Usuario Deletado com sucesso")
        return super().form_valid(form)
    
    