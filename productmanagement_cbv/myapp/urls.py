from django.urls import path
from myapp.views import home,ProductAPI,product_detail_view

urlpatterns = [
    path('', home,name='home'),
    path('api/products/', ProductAPI.as_view(),name='products'),
    path('api/products/<int:id>/', ProductAPI.as_view(),name='product'),
    path('product/<int:id>/', product_detail_view,name='product_detail'),
]
