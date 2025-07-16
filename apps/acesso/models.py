import uuid
from django.db import models
from django.db.models.signals import post_migrate
from django.contrib.auth.models import AbstractUser

from apps.clientes.models import TipoServicos


class CustomUser(AbstractUser):
    slug = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    nome_completo = models.CharField(max_length=150, blank=True)
    tipos_servicos = models.ManyToManyField(TipoServicos, blank=True)

    def save(self, *args, **kwargs):
        self.nome_completo = f"{self.first_name} {self.last_name}".strip()
        super().save(*args, **kwargs)
        

def usuario_deletado(sender, **kwargs):
    "Retorna/Cria um usuario para substituir usuarios deletados."
    user, create = CustomUser.objects.get_or_create(username='substituto', defaults={'first_name':'Usuário', 'last_name':'Deletado'})
    return user

post_migrate.connect(usuario_deletado)