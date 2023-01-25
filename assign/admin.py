from django.contrib import admin

# Register your models here.
from .models import Product_main_model, Product_image_model, Product_colour_model

admin.site.register(Product_main_model)
admin.site.register(Product_image_model)
admin.site.register(Product_colour_model)
