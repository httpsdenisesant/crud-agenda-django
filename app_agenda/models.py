from django.db import models

class Tarefa(models.Model):
    tarefa = models.CharField(max_length=100)
    prazo = models.DateField()

    def __str__(self):
        return self.tarefa
