from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import ItemForm
from ..models import Item
from ..services import buylist_service, item_service


@login_required()
def item_list(request, id):
    buylist_db = buylist_service.buylist_list_id(id)

    if buylist_db.user != request.user:
        return HttpResponse('Não Permitido!')

    item_db = item_service.list_item_by_buylist(buylist_db, request.user)

    return render(request, 'buylist/item_list.html',
                  {'items': item_db,
                   'buylist_id': id})


@login_required()
def register_item(request, id):
    buylist_db = buylist_service.buylist_list_id(id)

    if buylist_db.user != request.user:
        return HttpResponse('Não Permitido!')

    if request.method == 'POST':
        form_item = ItemForm(request.user, request.POST)

        if form_item.is_valid():
            buylist = buylist_service.buylist_list_id(id)

            product = form_item.cleaned_data['product']
            amount = form_item.cleaned_data['amount']
            unit = form_item.cleaned_data['unit']
            notes = form_item.cleaned_data['notes']

            new_item = Item(buylist=buylist, product=product, amount=amount,
                            unit=unit, notes=notes, user=request.user)

            item_service.register_item(new_item)
            return redirect('item_list_route', buylist.id)

    else:
        form_item = ItemForm(request.user)

    return render(request, 'buylist/form_item.html',
                  {'form_item': form_item, 'buylist_id': id})


@login_required()
def edit_item(request, id):
    item_db = item_service.item_by_id(id)

    if item_db.user != request.user:
        return HttpResponse('Não Permitido!')

    form_item = ItemForm(request.user, request.POST or None,
                         instance=item_db)

    if form_item.is_valid():
        item = item_service.item_by_id(id)
        product = form_item.cleaned_data['product']
        amount = form_item.cleaned_data['amount']
        unit = form_item.cleaned_data['unit']
        notes = form_item.cleaned_data['notes']

        new_item = Item(buylist=item.buylist, product=product, amount=amount,
                        unit=unit, notes=notes, user=request.user)

        item_service.edit_item(item_db, new_item)
        return redirect('item_list_route', item.buylist.id)

    return render(request, 'buylist/form_item.html',
                  {'form_item': form_item, 'buylist_id': item_db.buylist.id})


@login_required()
def remove_item(request, id):
    item_db = item_service.item_by_id(id)

    if item_db.user != request.user:
        return HttpResponse('Não Permitido!')

    if request.method == 'POST':
        buylist_id = item_db.buylist.id
        item_service.remove_item(item_db)
        return redirect('item_list_route', buylist_id)

    return render(request, 'buylist/remove_item_confirmation.html',
                  {'item': item_db})
