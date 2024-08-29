from django.db import models

class Aluno(models.Model):
    CIDADES_CHOICES = [
        ('SP', 'São Paulo'),
        ('RJ', 'Rio de Janeiro'),
        ('BH', 'Belo Horizonte'),
        ('RN', 'Natal'),
        ('RN', 'Paraná'),
        ('RN', 'Pau dos Ferros'),
        ('RN', 'São Miguel'),
        ('RN', 'Alexandria'),
        ('RN', 'Tenente Ananias'),
        ('CE', 'Pereiro')
    ]

    CURSO_CHOICES = [
        ('CS', 'Ciência da Computação'),
        ('ENG', 'Engenharia'),
        ('ADM', 'Administração'),
        ('MED', 'Medicina'),
        ('ENF', 'Enfermagem'),
    ]

    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=2, choices=CIDADES_CHOICES)
    email = models.EmailField()
    curso = models.CharField(max_length=3, choices=CURSO_CHOICES)

    def __str__(self):
        return self.nome
