from django.urls import path
from product.views import product_add, product_list, product_detail,product_edit,product_delete

urlpatterns = [
    path('list/',product_list, name='product_list'),
    path('<int:pk>/',product_detail, name='product_detail'),
    path('add/',product_add, name='product_add'),
    path('<int:pk>/edit/',product_edit, name='product_edit'),
    path('<int:pk>/delete/',product_delete, name='product_delete'),
]