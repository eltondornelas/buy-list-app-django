import buylist
from ..models import BuyList, BuyListItem


def register_buylist(buylist):
    BuyList.objects.create(name=buylist.name, user=buylist.user)


def buylist_list(user):
    return BuyList.objects.filter(user=user).all()


def buylist_list_id(id):
    return BuyList.objects.get(id=id)


def edit_buylist(buylist_db, new_buylist):
    buylist_db.name = new_buylist.name
    buylist_db.save(force_update=True)


def remove_buylist(buylist_db):
    buylist_db.delete()


def list_itens_by_buylist(buylist_item, user):
    return BuyListItem.objects.filter(buylist=buylist_item, user=user).all()


def item_by_id(id):
    return BuyListItem.objects.get(id=id)


def register_buylist_itens(buylist_item):
    BuyListItem.objects.create(buylist=buylist_item.buylist,
                               product=buylist_item.product,
                               amount=buylist_item.amount,
                               unit=buylist_item.unit,
                               notes=buylist_item.notes)


def edit_buylist_item(buylist_item_db, new_buylist_item):
    buylist_item_db.buylist = new_buylist_item.buylist
    buylist_item_db.product = new_buylist_item.product
    buylist_item_db.amount = new_buylist_item.amount
    buylist_item_db.unit = new_buylist_item.unit
    buylist_item_db.notes = new_buylist_item.notes

    buylist_item_db.save(force_update=True)


def remove_buylist_item(buylist_item_db):
    buylist_item_db.delete()
