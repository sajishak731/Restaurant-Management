
from django.urls import path
from AdminApp import views


urlpatterns = [
    path('login/', views.loginpage, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('Categories_Add/',views.Categories_Add,name="Categories_Add"),
    path('Category_Save/', views.Category_Save, name="Category_Save"),
    path('Category_View/', views.Category_View, name="Category_View"),
    path('Category_Edit/<int:t_id>', views.Category_Edit, name="Category_Edit"),
    path('Category_update/<int:c_id>', views.Category_update, name="Category_update"),
    path('Category_delete/<int:c_id>', views.Category_delete, name="Category_delete"),

    path('Food_Add/', views.Food_Add, name="Food_Add"),
    path('Food_Save/', views.Food_Save, name="Food_Save"),
    path('food_view/', views.food_view, name="food_view"),
    path('Food_Edit/<int:c_id>', views.Food_Edit, name="Food_Edit"),
    path('Food_update/<int:c_id>', views.Food_update, name="Food_update"),
    path('Food_delete/<int:c_id>', views.Food_delete, name="Food_delete"),

    path('Staff_add/', views.Staff_add, name="Staff_add"),
    path('Staff_Save/', views.Staff_Save, name="Staff_Save"),
    path('Staff_View/', views.Staff_View, name="Staff_View"),
    path('Staff_Edit/<int:t_id>', views.Staff_Edit, name="Staff_Edit"),
    path('Staff_Update/<int:s_id>', views.Staff_Update, name="Staff_Update"),

    path('Staff_Delete/<int:c_id>', views.Staff_Delete, name="Staff_Delete"),

]
