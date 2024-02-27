from django.db import models

# Create your models here.
class Tarefa(models.Model):
    nome = models.CharField('nome', max_length=200)

class Academy(models.Model):
    nome = models.CharField('nome', max_length=200)

class Programation(models.Model):
    nome = models.CharField('nome', max_length=100, null=False, blank=False)
    def __str__(self) -> str:
        return self.nome
    
class Faxina(models.Model):
    nome = models.CharField('nome', max_length=100, null=False, blank=False)
    def __str__(self) -> str:
        return self.nome