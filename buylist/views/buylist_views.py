from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import BuyListForm
from ..models import BuyList
from ..services import buylist_service


@login_required()
def buylist_list(request):
    buylists = buylist_service.buylist_list(request.user)
    return render(request, 'buylist/buylist_list.html', {'buylists': buylists})


@login_required()
def register_buylist(request):
    if request.method == 'POST':
        form_buylist = BuyListForm(request.POST)

        if form_buylist.is_valid():
            name = form_buylist.cleaned_data['name']

            new_buylist = BuyList(name=name, user=request.user)
            buylist_service.register_buylist(new_buylist)

            return redirect('buylist_list_route')

    else:
        form_buylist = BuyListForm()

    return render(request, 'buylist/form_buylist.html',
                  {'form_buylist': form_buylist})


@login_required()
def edit_buylist(request, id):
    buylist_db = buylist_service.buylist_list_id(id)

    if buylist_db.user != request.user:
        return HttpResponse('Não Permitido!')

    form_buylist = BuyListForm(request.POST or None, instance=buylist_db)

    if form_buylist.is_valid():
        name = form_buylist.cleaned_data['name']

        new_buylist = BuyList(name=name, user=request.user)
        buylist_service.edit_buylist(buylist_db, new_buylist)

        return redirect('buylist_list_route')

    return render(request, 'buylist/form_buylist.html',
                  {'form_buylist': form_buylist})


@login_required()
def remove_buylist(request, id):
    buylist_db = buylist_service.buylist_list_id(id)

    if buylist_db.user != request.user:
        return HttpResponse('Não Permitido!')

    if request.method == 'POST':
        buylist_service.remove_buylist(buylist_db)
        return redirect('buylist_list_route')

    return render(request, 'buylist/remove_buylist_confirmation.html',
                  {'buylist': buylist_db})
