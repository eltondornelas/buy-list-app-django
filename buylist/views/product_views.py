from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import ProductForm
from ..models import Product
from ..services import product_service


@login_required()
def product_list(request):
    products = product_service.product_list(request.user)
    return render(request, 'buylist/product_list.html', {'products': products})


@login_required()
def register_product(request):
    if request.method == 'POST':
        form_product = ProductForm(request.POST)

        if form_product.is_valid():
            description = form_product.cleaned_data['description']
            brand = form_product.cleaned_data['brand']
            section = form_product.cleaned_data['section']

            new_product = Product(description=description, brand=brand,
                                  section=section,
                                  user=request.user)
            product_service.register_product(new_product)

            return redirect('product_list_route')

    else:
        form_product = ProductForm()

    return render(request, 'buylist/form_product.html',
                  {'form_product': form_product})


@login_required()
def edit_product(request, id):
    product_db = product_service.product_list_id(id)

    if product_db.user != request.user:
        return HttpResponse('Não Permitido!')
        # TODO: criar uma página mais decente aqui

    form_product = ProductForm(request.POST or None, instance=product_db)

    if form_product.is_valid():
        description = form_product.cleaned_data['description']
        brand = form_product.cleaned_data['brand']
        section = form_product.cleaned_data['section']
        new_product = Product(description=description, brand=brand,
                              section=section, user=request.user)

        product_service.edit_product(product_db, new_product)
        return redirect('product_list_route')

    return render(request, 'buylist/form_product.html',
                  {'form_product': form_product})


@login_required()
def remove_product(request, id):
    product_db = product_service.product_list_id(id)

    if product_db.user != request.user:
        return HttpResponse('Não Permitido!')

    if request.method == 'POST':
        product_service.remove_product(product_db)
        return redirect('product_list_route')

    return render(request, 'buylist/remove_product_confirmation.html',
                  {'product': product_db})
