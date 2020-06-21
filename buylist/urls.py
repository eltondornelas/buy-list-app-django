from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from .views.product_views import *
from .views.buylist_views import *
from .views.item_views import *
from .views.user_views import *

urlpatterns = [
    # path('', RedirectView.as_view(url='/buylist_list/')),
    path('', buylist_list),

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

    path('item_list/<int:id>', item_list, name='item_list_route'),
    path('register_item/<int:id>', register_item, name='register_item_route'),
    path('edit_item/<int:id>', edit_item, name='edit_item_route'),
    path('remove_item/<int:id>', remove_item, name='remove_item_route'),

    path('register_user/', register_user, name='register_user_route'),
    path('login_user/', login_user, name='login_user_route'),
    path('logout_user/', logout_user, name='logout_user_route'),
]
