from ..models import Product


def register_product(product):
    Product.objects.create(description=product.description,
                           brand=product.brand, user=product.user)


def product_list(user):
    return Product.objects.filter(user=user).all()
    # SELECT * FROM buylist_product


def product_list_id(id):
    return Product.objects.get(id=id)


def edit_product(product_db, new_product):
    product_db.description = new_product.description
    product_db.brand = new_product.brand

    product_db.save(force_update=True)
    # o force é para indicar que é uma atualização


def remove_product(product_db):
    product_db.delete()
