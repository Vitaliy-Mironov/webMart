from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.cart_datail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('save/', views.cart_save, name='cart_save'),
    path('sale/', views.cart_sale, name='cart_sale'),
]
