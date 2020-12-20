
from django.urls import path
from .views import (
    
    home ,
    products,
    customer,
    createOrder,
    updateOrder,
    deleteOrder 
    
    )

urlpatterns = [
    path('', home, name="home" ),
    path('products', products, name="products" ),
    path('customer/<int:pk>', customer, name="customer" ),
    
    path('create_order/', createOrder, name="create_order" ),
    path('update_order/<int:pk>', updateOrder, name="update_order" ),
    path('delete_order/<int:pk>', deleteOrder, name="delete_order" ),


]
