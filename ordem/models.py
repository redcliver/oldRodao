from django.db import models
from django.utils import timezone
from cliente.models import cliente
from servico.models import servico
from produto.models import produto
from funcionario.models import funcionario

# Create your models here.

class produto_item(models.Model):
    id = models.AutoField(primary_key=True)
    prod_item = models.ForeignKey(produto)
    quantidade = models.IntegerField(default='1')
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __int__(self):
        return self.id

class servico_item(models.Model):
    id = models.AutoField(primary_key=True)
    serv_item = models.ForeignKey(servico)
    quantidade = models.IntegerField(default='1')
    func = models.ForeignKey(funcionario)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __int__(self):
        return self.id


class ordens(models.Model):
    ESTADO = (
        ('1', 'Em Aberto'),
        ('2', 'Finalizada'),
    )
    METODO = (
        ('1', 'Dinheiro'),
        ('2', 'Cartao Debito'),
        ('3', 'Cartao Credito'),
    )
    id = models.AutoField(primary_key=True)
    cliente_ordem = models.ForeignKey(cliente)
    prod_item = models.ManyToManyField(produto_item)
    serv_item = models.ManyToManyField(servico_item)
    estado = models.CharField(max_length=1, choices=ESTADO)
    metodo = models.CharField(max_length=1, choices=METODO, null=True, blank=True)
    data_abertura = models.DateTimeField(default=timezone.now)
    data_fechamento = models.DateTimeField(null=True, blank=True)
    carro = models.CharField(max_length=100, null=True, blank=True)
    placa = models.CharField(max_length=10, null=True, blank=True)
    desc = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.id)