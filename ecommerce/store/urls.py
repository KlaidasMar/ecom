from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('news', views.newsPage, name="news"),
    path('phones/', views.phones, name="phones"),
    path('tablets/', views.tablets, name="tablets"),
    path('watches/', views.watches, name="watches"),
    path('services/', views.services, name="services"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]