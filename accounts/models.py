from django.db import models

class AlunoUnivesp(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        black=False
    )
    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    matricula = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    objetos = models.Manager()
