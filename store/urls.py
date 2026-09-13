from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('about/', views.about_us, name='about_us'),
    path('dashboard/add-product/', views.add_product_custom, name='add_product_custom'),
]