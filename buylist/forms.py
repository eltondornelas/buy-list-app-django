from django import forms
from .models import Product, BuyList, BuyListItem


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class BuyListForm(forms.ModelForm):
    class Meta:
        model = BuyList
        fields = '__all__'


class BuyListItemForm(forms.ModelForm):
    class Meta:
        model = BuyListItem
        fields = '__all__'
