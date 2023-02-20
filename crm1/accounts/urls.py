from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
    path('users/',views.users),
    path('add_products/',views.Add_products),
    path('create_order/', views.createOrder, name="create_order"),
    path('user_delete/', views.deleteUser, name="user_delete"),
    

] 