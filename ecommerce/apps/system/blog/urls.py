
from    django.urls import path
from    .views      import (
        
    createOrder,
    updateOrder,
    deleteOrder,
    
    )

urlpatterns = [

    path('create_order/',           createOrder,    name = "create_order" ),
    path('update_order/<int:pk>',   updateOrder,    name = "update_order" ),
    path('delete_order/<int:pk>',   deleteOrder,    name = "delete_order" ),

]
