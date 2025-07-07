import re
from django.contrib.auth.models import User, Permission, Group
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView

from apps.acesso.models import CustomUser
from apps.clientes.models import TipoServicos


class PermServicos(UpdateView):
    model = CustomUser
    fields = ['tipos_servicos']
    template_name='acesso/usuarios/perm_servicos.html'
    
    def get_success_url(self):
        return reverse('listagem_usuarios')
    
    def get_object(self, queryset = None):
        if 'user' in self.request.POST and self.request.POST['user']:
            user_id = self.request.POST['user']
        else:
            user_id = self.kwargs['pk']
        object = CustomUser.objects.get(id=user_id)
        return object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_title'] = 'Edição'
        context['subtitle'] = 'Aqui você edita os Tipos de Serviço que o Usuário {} pode executar.'.format(self.object.nome_completo)
        context['form'] = self.get_form()
        context['tipos_servicos'] = TipoServicos.objects.all()
        context['tipos_servicos_selected'] = list(self.object.tipos_servicos.all().values_list('id',flat=True))
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro na Edição do Usuario. {}".format(form.errors))
        return HttpResponseRedirect(self.get_success_url())
        
    def form_valid(self, form):
        messages.success(self.request, "Usuario salvo com sucesso")
        return super().form_valid(form)
    
    