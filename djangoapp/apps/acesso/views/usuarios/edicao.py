import re
from django.contrib.auth.models import User, Permission, Group
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.views.generic import UpdateView

from apps.acesso.forms import CustomUserChangeForm



class EdiUsuarios(UpdateView):
    model = User
    template_name='acesso/usuarios/edicao.html'
    form_class = CustomUserChangeForm
    
    def get_success_url(self):
        return reverse('listagem_usuarios')
    
    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Usuarios',
                'url': None,
                'activate': 'true'
            },{
                'title': 'Edição',
                'url': None,
                'activate': 'true'
            }
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Usuarios'
        context['card_title'] = 'Edição'
        context['subtitle'] = 'Aqui você edita os Usuarios.'
        context['form'] = self.get_form()
        context['permissions'] = Permission.objects.filter().exclude(content_type_id__in=[1,5,6,8,9])
        user_permissions_list = ",".join([str(x) for x in self.object.user_permissions.all().values_list('id',flat=True)])
        groups_list = ",".join([str(x) for x in self.object.groups.all().values_list('id',flat=True)])
        context['user_permissions'] = "({})".format(user_permissions_list)
        context['user_groups'] = "({})".format(groups_list)
        context['groups'] = Group.objects.all()
        return context
    
    def get_form_kwargs(self):
        kwargs = super(EdiUsuarios, self).get_form_kwargs()

        if self.request.method in ('POST', 'PUT'):
            data = self.request.POST.copy()
            date_joined = self.object.date_joined
            data.update({'date_joined': date_joined})
            kwargs.update({'data': data})

        return kwargs
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro na Edição do Usuario. {}".format(form.errors))
        return super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, "Usuario salvo com sucesso")
        return super().form_valid(form)
    
    