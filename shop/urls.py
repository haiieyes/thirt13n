from django.urls import path, include
from shop.views import catalogue

urlpatterns = [
    path('', catalogue, name='catalogue')
]