from django.urls import path
from .views import get_all_products, product_detail
urlpatterns = [
    path("products/", get_all_products),
    path("products/<str:id>/", product_detail)
]
