from django import forms
from .models import Product, BuyList, Item


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


class ItemForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(user=user)

    class Meta:
        model = Item
        exclude = ('user',)
        fields = '__all__'
