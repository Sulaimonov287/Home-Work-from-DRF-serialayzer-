from django.urls import path
from .models import *
from .views import get_one_product, get_products, update_product, delete_product, create_product

urlpatterns = [
    path('create/', create_product, name='products'),
    path('update/product/<int:pk>/', update_product, name='products'),
    path('delete/product/<int:pk>/', delete_product, name='products'),
]
