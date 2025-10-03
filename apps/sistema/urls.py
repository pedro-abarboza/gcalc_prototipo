from django.urls import path

from apps.sistema.views import SistemaView


urlpatterns = [
    path('', SistemaView.as_view(), name='sistema'),
]