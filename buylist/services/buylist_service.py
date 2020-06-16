import buylist
from ..models import BuyList, BuyListItem


def register_buylist(buylist):
    BuyList.objects.create(name=buylist.name)


def buylist_list():
    return BuyList.objects.all()


def buylist_list_id(id):
    return BuyList.objects.get(id=id)


def edit_buylist(buylist_db, new_buylist):
    buylist_db.name = new_buylist.name

    buylist_db.save(force_update=True)


def remove_buylist(buylist_db):
    buylist_db.delete()


def list_itens_by_buylist_id(buylist_item):
    return BuyListItem.objects.filter(buylist=buylist_item)


def register_buylist_itens(buylist_item):
    BuyListItem.objects.create(buylist=buylist_item.buylist,
                               product=buylist_item.product,
                               amount=buylist_item.amount,
                               unit=buylist_item.unit,
                               notes=buylist_item.notes)
