from django.urls import path
from . import views


urlpatterns = [
    path('products/',views.ProductsView.as_view(), name='products_view'),
    path('products/<id_args>/',views.ProductView.as_view(), name='product_view'),
]