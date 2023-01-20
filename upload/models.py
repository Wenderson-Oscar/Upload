from django.db import models

# Create your models here.
class Pessoa(models.Model):

    codigo = models.IntegerField(blank=True)
    nome = models.CharField(max_length=100, blank=True)
    sobrenome = models.CharField(max_length=100, blank=True)
    sexo = models.CharField(max_length=1, blank=True)
    altura = models.CharField(max_length=100, blank=True)
    peso = models.CharField(max_length=100, blank=True)
    nascimento = models.DateField(blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=1, blank=True)
    file = models.FileField(upload_to='upload/media')
