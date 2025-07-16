import json
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView


class Login(LoginView):
    template_name='acesso/usuarios/login.html'
    next_page = 'home'


class AutoCompUsuarios(View):

    def get(self, *args, **kwargs):
        text = self.request.GET['term']
        result = list(User.objects.filter(first_name__icontains=text).values_list('first_name',flat=True))
        data = json.dumps(result)
        return HttpResponse(data, 'application/json')