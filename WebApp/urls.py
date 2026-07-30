from django.urls import path
from WebApp import views


urlpatterns= [
    path('home/',views.home,name="home"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('user_sign_up/', views.user_sign_up, name="user_sign_up"),
    path('user_sign_in/', views.user_sign_in, name="user_sign_in"),
    path('user_logout/', views.user_logout, name="user_logout"),

    path('menu/', views.menu, name="menu"),
    path('add_cart/', views.add_cart, name="add_cart"),

]