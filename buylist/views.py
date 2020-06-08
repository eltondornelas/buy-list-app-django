from django.shortcuts import render


def product_list(request):
    product = {'description': 'detergente', 'brand': 'limpol'}

    return render(request, 'buylist/product_list.html', {'product': product})
