from ..models import Item


def list_item_by_buylist(buylist, user):
    return Item.objects.filter(buylist=buylist, user=user).all()


def item_by_id(id):
    return Item.objects.get(id=id)


def register_item(item):
    Item.objects.create(buylist=item.buylist,
                        product=item.product,
                        amount=item.amount,
                        unit=item.unit,
                        notes=item.notes,
                        user=item.user)


def edit_item(item_db, new_item):
    item_db.buylist = new_item.buylist
    item_db.product = new_item.product
    item_db.amount = new_item.amount
    item_db.unit = new_item.unit
    item_db.notes = new_item.notes

    item_db.save(force_update=True)


def remove_item(item_db):
    item_db.delete()
