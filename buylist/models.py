from django.db import models


class Product(models.Model):
    description = models.CharField(max_length=100, null=False, blank=False,
                                   verbose_name='Descrição')
    brand = models.CharField(max_length=24, verbose_name='Marca', null=True,
                             blank=True)

    def __str__(self):
        return f'{self.description} - {self.brand}'


class BuyList(models.Model):
    name = models.CharField(max_length=48, null=False, blank=False)

    def __str__(self):
        return self.name


class BuyListItem(models.Model):
    buylist = models.ForeignKey(BuyList, on_delete=models.CASCADE, null=True,
                                blank=True, verbose_name='Lista de Compras')
    # buylist permite ser nulo, pois será automaticamente preenchido na lógica
    # do views, sem ser dessa forma ele não passa no is_valid()

    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Produto', null=False,
                                blank=False)
    amount = models.FloatField(verbose_name='Quantidade', null=False,
                               blank=False)
    unit = models.CharField(max_length=10, verbose_name='Unidade', null=False,
                            blank=False)
    notes = models.TextField(verbose_name='Observações', null=False,
                             blank=False)

    def __str__(self):
        return f'{self.buylist.id}'
