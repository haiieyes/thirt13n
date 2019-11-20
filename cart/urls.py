from django.urls import path, include
from .views import add_to_cart, view, remove_from_cart
from shop.views import catalogue

urlpatterns = [
    path('add_to_cart/<product_id>', add_to_cart, name='add_to_cart'),
    path('', view, name='view'),
    path('remove_from_cart/<cart_item_id>', remove_from_cart, name='remove_from_cart'),
    path('shop/', include('shop.urls'))
]