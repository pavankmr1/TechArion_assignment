from django.db import models
import uuid

# Create your models here.


class Product_main_model(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    price = models.IntegerField(null=True)
    unique_code = models.UUIDField(default=uuid.uuid4, unique=True)
    size = models.IntegerField(choices=[(10, '10'), (20, '20'), (30, '30')])
    quality = models.CharField(max_length=255, choices=[(
        'high', 'high'), ('low', 'low'), ('medium', 'medium')])


class Product_colour_model(models.Model):
    product = models.ForeignKey(
        Product_main_model, related_name="colour", on_delete=models.CASCADE)
    colour = models.CharField(max_length=255, choices=[(
        'red', 'red'), ('green', 'green'), ('black', 'black'), ('blue', 'blue')])


class Product_image_model(models.Model):
    product = models.ForeignKey(
        Product_main_model, related_name="image", on_delete=models.CASCADE)
    image = models.ImageField()
