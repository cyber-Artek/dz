from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('admin-products/', views.admin_products, name='admin_products'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('cart/', views.user_cart, name='user_cart'),
]

