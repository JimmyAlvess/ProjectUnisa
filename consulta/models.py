
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Categoria(models.Model):
    especialidade = models.CharField(max_length=75)

    def __str__(self) -> str:
        return self.especialidade


class Medico(models.Model):

    nome_completo = models.CharField(max_length=75)
    idade = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)
    crm = models.CharField(max_length=20)
    endereco = models.CharField(max_length=80)
    cep = models.CharField(max_length=30)
    publicado = models.BooleanField(default=False)
    img = models.ImageField(upload_to='home/covers/%Y/%m/%d/')
    especialidade = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True
    )
    autor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.nome_completo


class Paciente(models.Model):

    nome_completo = models.CharField(max_length=75)
    idade = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=9)
    data = models.DateField()

    def __str__(self) -> str:
        return self.nome_completo
