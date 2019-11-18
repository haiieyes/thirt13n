from django.urls import path, include
from .views import catalogue

urlpatterns = [
    path('', catalogue, name='catalogue')
]