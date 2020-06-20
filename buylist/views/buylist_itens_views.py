from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import BuyListItemForm
from ..models import BuyListItem
from ..services import buylist_service


@login_required()
def buylist_list_itens(request, id):
    buylist_db = buylist_service.buylist_list_id(id)

    # achei necessário aqui por conta da url ter <id> e era possível acessar
    # a página direto pela url, mesmo que não mostrasse dados
    if buylist_db.user != request.user:
        return HttpResponse('Não Permitido!')

    buylist_item_db = buylist_service.list_itens_by_buylist(buylist_db,
                                                            request.user)

    return render(request, 'buylist/buylist_list_itens.html',
                  {'buylist_itens': buylist_item_db,
                   'buylist_id': id})


@login_required()
def register_buylist_itens(request, id):
    buylist_db = buylist_service.buylist_list_id(id)

    if buylist_db.user != request.user:
        return HttpResponse('Não Permitido!')

    if request.method == 'POST':
        form_buylist_itens = BuyListItemForm(request.POST)

        if form_buylist_itens.is_valid():
            buylist = buylist_service.buylist_list_id(id)

            product = form_buylist_itens.cleaned_data['product']
            amount = form_buylist_itens.cleaned_data['amount']
            unit = form_buylist_itens.cleaned_data['unit']
            notes = form_buylist_itens.cleaned_data['notes']

            new_buylist_item = BuyListItem(buylist=buylist, product=product,
                                           amount=amount, unit=unit,
                                           notes=notes, user=request.user)

            buylist_service.register_buylist_itens(new_buylist_item)
            return redirect('buylist_list_itens_route', buylist.id)

    else:
        form_buylist_itens = BuyListItemForm()

    return render(request, 'buylist/form_buylist_itens.html',
                  {'form_buylist_itens': form_buylist_itens})


@login_required()
def edit_buylist_itens(request, id):
    buylist_item_db = buylist_service.item_by_id(id)

    if buylist_item_db.user != request.user:
        return HttpResponse('Não Permitido!')

    form_buylist_itens = BuyListItemForm(request.POST or None,
                                         instance=buylist_item_db)

    if form_buylist_itens.is_valid():
        item = buylist_service.item_by_id(id)
        product = form_buylist_itens.cleaned_data['product']
        amount = form_buylist_itens.cleaned_data['amount']
        unit = form_buylist_itens.cleaned_data['unit']
        notes = form_buylist_itens.cleaned_data['notes']

        new_buylist_item = BuyListItem(buylist=item.buylist, product=product,
                                       amount=amount, unit=unit, notes=notes)

        buylist_service.edit_buylist_item(buylist_item_db, new_buylist_item)
        return redirect('buylist_list_itens_route', item.buylist.id)

    return render(request, 'buylist/form_buylist_itens.html',
                  {'form_buylist_itens': form_buylist_itens})


@login_required()
def remove_buylist_itens(request, id):
    buylist_item_db = buylist_service.item_by_id(id)

    if buylist_item_db.user != request.user:
        return HttpResponse('Não Permitido!')

    if request.method == 'POST':
        buylist_id = buylist_item_db.buylist.id
        buylist_service.remove_buylist_item(buylist_item_db)
        return redirect('buylist_list_itens_route', buylist_id)

    return render(request, 'buylist/remove_buylist_item_confirmation.html',
                  {'item': buylist_item_db})
