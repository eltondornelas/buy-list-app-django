from ..models import BuyList


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
