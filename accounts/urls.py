from django.urls import path, include
from accounts.views import index, album, music, shop, logout, login, register

urlpatterns = [
    path('', index, name='index'),
    path('album/', album, name='album'),
    path('music/', music, name='music'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('register/', register, name='register')
]