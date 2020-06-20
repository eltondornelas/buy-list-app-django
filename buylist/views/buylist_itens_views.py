from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ..forms import BuyListItemForm
from ..models import BuyListItem
from ..services import buylist_service


@login_required()
def buylist_list_itens(request, id):
    buylist_db = buylist_service.buylist_list_id(id)
    buylist_item_db = buylist_service.list_itens_by_buylist(buylist_db)

    # current_path = str(request.get_full_path())
    #  no template: {{ request.get_full_path }}

    return render(request, 'buylist/buylist_list_itens.html',
                  {'buylist_itens': buylist_item_db,
                   'buylist_id': id})


@login_required()
def register_buylist_itens(request, id):
    if request.method == 'POST':
        # print(request.POST['buylist'])
        form_buylist_itens = BuyListItemForm(request.POST)
        print('cheguei aqui 1')

        # TODO: digitando pela url/x ele abre o formulário, ajustar!

        if form_buylist_itens.is_valid():
            print('cheguei aqui 2')
            # buylist = form_buylist_itens.cleaned_data['buylist']

            buylist = buylist_service.buylist_list_id(id)

            product = form_buylist_itens.cleaned_data['product']
            amount = form_buylist_itens.cleaned_data['amount']
            unit = form_buylist_itens.cleaned_data['unit']
            notes = form_buylist_itens.cleaned_data['notes']

            new_buylist_item = BuyListItem(buylist=buylist, product=product,
                                           amount=amount, unit=unit,
                                           notes=notes)

            buylist_service.register_buylist_itens(new_buylist_item)
            return redirect('buylist_list_itens_route', buylist.id)

    else:
        form_buylist_itens = BuyListItemForm()

    return render(request, 'buylist/form_buylist_itens.html',
                  {'form_buylist_itens': form_buylist_itens})


@login_required()
def edit_buylist_itens(request, id):
    buylist_item_db = buylist_service.item_by_id(id)
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

    if request.method == 'POST':
        buylist_id = buylist_item_db.buylist.id
        buylist_service.remove_buylist_item(buylist_item_db)
        return redirect('buylist_list_itens_route', buylist_id)

    return render(request, 'buylist/remove_buylist_item_confirmation.html',
                  {'item': buylist_item_db})
