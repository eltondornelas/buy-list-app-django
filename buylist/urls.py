from django.contrib import admin
from django.urls import path
from .views.product_views import *
from .views.buylist_views import *
from .views.buylist_itens_views import *


urlpatterns = [
    path('register_product/', register_product, name='register_product_route'),
    path('product_list/', product_list, name='product_list_route'),
    path('edit_product/<int:id>', edit_product, name='edit_product_route'),
    path('remove_product/<int:id>', remove_product,
         name='remove_product_route'),

    path('buylist_list/', buylist_list, name='buylist_list_route'),
    path('register_buylist/', register_buylist, name='register_buylist_route'),
    path('edit_buylist/<int:id>', edit_buylist, name='edit_buylist_route'),
    path('remove_buylist/<int:id>', remove_buylist,
         name='remove_buylist_route'),

    path('buylist_list_itens/<int:id>', buylist_list_itens,
         name='buylist_list_itens_route'),
    path('register_buylist_itens/<int:id>', register_buylist_itens,
         name='register_buylist_itens_route'),
]
