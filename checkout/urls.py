from django.urls import path, include
from .views import charge

urlpatterns = [
    path('', charge, name='charge')
]