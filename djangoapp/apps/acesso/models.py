import uuid
from django.db import models
from django.contrib.auth.models import User
from apps.clientes.models import TipoServicos
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    slug = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    nome_completo = models.CharField(max_length=150, blank=True)
    tipos_servicos = models.ManyToManyField(TipoServicos, blank=True)

    def save(self, *args, **kwargs):
        self.nome_completo = f"{self.first_name} {self.last_name}".strip()
        super().save(*args, **kwargs)



@property
def nome_completo(self):
    return f"{self.first_name} {self.last_name}".strip()

User.add_to_class("nome_completo", nome_completo)