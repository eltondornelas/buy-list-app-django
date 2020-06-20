from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ..forms import ProductForm
from ..models import Product
from ..services import product_service


@login_required()
def product_list(request):
    products = product_service.product_list()
    return render(request, 'buylist/product_list.html', {'products': products})


@login_required()
def register_product(request):
    if request.method == 'POST':
        form_product = ProductForm(request.POST)
        # quando passa o parâmetro ele já verifica/valida automaticamente

        if form_product.is_valid():
            description = form_product.cleaned_data['description']
            brand = form_product.cleaned_data['brand']

            new_product = Product(description=description, brand=brand)
            product_service.register_product(new_product)

            return redirect('product_list_route')

    else:
        form_product = ProductForm()

    return render(request, 'buylist/form_product.html',
                  {'form_product': form_product})


@login_required()
def edit_product(request, id):
    product_db = product_service.product_list_id(id)
    form_product = ProductForm(request.POST or None, instance=product_db)
    # lembrando que a partir daqui é após ser clicado para atualizar

    if form_product.is_valid():
        description = form_product.cleaned_data['description']
        brand = form_product.cleaned_data['brand']

        new_product = Product(description=description, brand=brand)
        # importante sempre escrever param = arg, pois causou erro, sem ele
        product_service.edit_product(product_db, new_product)
        return redirect('product_list_route')

    return render(request, 'buylist/form_product.html',
                  {'form_product': form_product})


@login_required()
def remove_product(request, id):
    product_db = product_service.product_list_id(id)

    if request.method == 'POST':
        product_service.remove_product(product_db)
        return redirect('product_list_route')

    return render(request, 'buylist/remove_product_confirmation.html',
                  {'product': product_db})
