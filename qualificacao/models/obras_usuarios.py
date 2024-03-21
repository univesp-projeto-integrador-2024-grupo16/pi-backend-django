from django.contrib.auth.models import User
from django.db import models

from .cadastro_obras import CadastroObras

from uuid import uuid4
from datetime import datetime

class ObrasUsuario(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        null=False,
        blank=False,
        default=uuid4,
        editable=False,
        unique=True
    )
    auth_user = models.ManyToManyField(User)
    obras = models.ManyToManyField(CadastroObras)
