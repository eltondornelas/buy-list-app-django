from ..models import Product


def register_product(product):
    Product.objects.create(description=product.description,
                           brand=product.brand, section=product.section,
                           user=product.user)


def product_list(user):
    return Product.objects.filter(user=user).all()


def product_list_id(id):
    return Product.objects.get(id=id)


def edit_product(product_db, new_product):
    product_db.description = new_product.description
    product_db.brand = new_product.brand
    product_db.section = new_product.section

    product_db.save(force_update=True)


def remove_product(product_db):
    product_db.delete()
