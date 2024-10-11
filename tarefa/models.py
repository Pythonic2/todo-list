from django.db import models
from authentication.models import CustomUser

# Create your models here.
class Tarefa(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40)
    descricao = models.CharField(max_length=100)
    criada = models.DateTimeField(auto_now_add=True)
    editada = models.DateTimeField(blank=True, null=True)
    concluida = models.BooleanField(default=False)


    def __str__(self):
        return f"Tarefa: {self.titulo}, Criada: {self.criada}, Editada: {self.editada}"