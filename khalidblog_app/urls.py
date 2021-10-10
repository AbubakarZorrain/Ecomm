from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import re_path

urlpatterns = [

path('',views.arsha, name="index"),
path('home/',views.navbar, name="index"),
path('accounts/login/',views.signin,name="login"),
path('logout',views.logout_view),
path('arsha', views.arsha, name="arsha"),
path('validate/', views.validate_username, name='validate_username'),
path('cart_add/', views.cart_add, name='cart_add'),
path('cart_add/', views.cart_add, name='cart_add'),
    path('item_increment/', views.item_increment, name='item_increment'),
    # path('item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    # path('cart_clear/', views.cart_clear, name='cart_clear'),
    # path('item_clear/<int:id>/', views.item_clear, name='item_clear'),



]