from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('product_list/', product_list, name='product_list_route'),
    path('edit_product/<int:id>', edit_product, name='edit_product_route'),
    path('register_product/', register_product, name='register_product_route'),
    path('remove_product/<int:id>', remove_product,
         name='remove_product_route'),
]
