from django.urls import path
from WebApp import views


urlpatterns= [
    path('home/',views.home,name="home"),
    path('about/', views.about, name="about"),
    path("my_orders/", views.my_orders, name="my_orders"),

    path('loginpage/', views.loginpage, name="loginpage"),
    path('user_sign_up/', views.user_sign_up, name="user_sign_up"),
    path('user_sign_in/', views.user_sign_in, name="user_sign_in"),
    path('user_logout/', views.user_logout, name="user_logout"),

    path('menu/', views.menu, name="menu"),
    path('add_cart/', views.add_cart, name="add_cart"),
    path('save_cart_items/',views.save_cart_items,name="save_cart_items"),
    path('view_cart/',views.view_cart,name="view_cart"),
    path('checkout/', views.checkout, name="checkout"),
    path("place_order/", views.place_order, name="place_order"),
    path("payment/", views.payment, name="payment"),
    path('payment_page/',views.payment_page,name="payment_page"),

    # path("book_table/", views.book_table, name="book_table"),
    path("book_table/", views.book_table, name="book_table"),
    path("booking_success/", views.booking_success, name="booking_success"),

]