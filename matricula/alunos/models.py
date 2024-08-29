from django.db import models

# Create your models here.

from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    email = models.EmailField()
    curso = models.CharField(max_length=100)

    def __str__(self):
       return self.nome
   
