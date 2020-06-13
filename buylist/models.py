from django.db import models


class Product(models.Model):
    description = models.CharField(max_length=100, null=False, blank=False,
                                   verbose_name='Descrição')
    brand = models.CharField(max_length=24, verbose_name='Marca', null=True,
                             blank=True)


class BuyList(models.Model):
    name = models.CharField(max_length=48, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Produto')
    amount = models.FloatField(verbose_name='Quantidade')
    unit = models.CharField(max_length=10, verbose_name='Unidade')
    notes = models.TextField(verbose_name='Observações')
