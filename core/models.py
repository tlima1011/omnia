from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    ncm = models.IntegerField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data_criacao = models.DateField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table ='produto'

    def __str__(self):
        return self.nome

