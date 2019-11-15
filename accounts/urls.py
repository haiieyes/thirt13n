from django.urls import path, include
from accounts.views import index, shop, logout, login, register

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('register/', register, name='register')
]