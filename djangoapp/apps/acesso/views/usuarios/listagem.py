import json
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView

from apps.acesso.models import CustomUser


class ListagemUsuarios(ListView):
    template_name='acesso/usuarios/listagem.html'
    model = CustomUser
    fields = ['id','username','first_name']

    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Usuarios',
                'url': '',
                'activate': None
            },{
                'title': 'Listagem',
                'url': '',
                'activate': 'true'
            }
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Usuarios'
        context['card_title'] = 'Listagem'
        context['subtitle'] = 'Aqui você tem a lista de todos os Usuarios cadastrados.'
        
        return context

class AutoCompUsuarios(View):

    def get(self, *args, **kwargs):
        text = self.request.GET['term']
        result = list(CustomUser.objects.filter(first_name__icontains=text).values_list('first_name',flat=True))
        data = json.dumps(result)
        return HttpResponse(data, 'application/json')