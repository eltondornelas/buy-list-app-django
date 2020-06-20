from django import forms
from .models import Product, BuyList, BuyListItem


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user',)
        # dessa forma só mantem o controle no backend, não fica no form
        # não há necessidade de incluir no formulário por segurança
        fields = '__all__'


class BuyListForm(forms.ModelForm):
    class Meta:
        model = BuyList
        exclude = ('user',)
        fields = '__all__'


class BuyListItemForm(forms.ModelForm):
    class Meta:
        model = BuyListItem
        exclude = ('user',)
        fields = '__all__'
