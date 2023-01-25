from django.shortcuts import render
from django.http import JsonResponse
from .models import Product_main_model, Product_image_model, Product_colour_model

# Create your views here.


def get_all_products(request):
    products = Product_main_model.objects.all()

    data = []
    for product in products:
        product_data = {
            "title": product.title,
            "description": product.description,
            "price": product.price,
            "unique_code": product.unique_code,
            "size": product.size,
            "quality": product.quality,
            "colors": [colour.colour for colour in product.colour.all()],
            "image": [image.image.url for image in product.image.all()]
        }
        data.append(product_data)

    return JsonResponse(list(data), safe=False)


def product_detail(request, id):
    products = Product_main_model.objects.get(unique_code=id)
    data = {
        "title": products.title,
        "description": products.description,
        "price": products.price,
        "unique_code": products.unique_code,
        "size": products.size,
        "quality": products.quality,
        "colors": [colour.colour for colour in products.colour.all()],
        "image": [image.image.url for image in products.image.all()]
    }

    return JsonResponse(data)
