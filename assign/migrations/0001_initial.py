# Generated by Django 4.1.3 on 2023-01-25 11:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_main_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_code', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('size', models.IntegerField(choices=[(10, '10'), (20, '20'), (30, '30')])),
                ('quality', models.CharField(choices=[('high', 'high'), ('low', 'low'), ('medium', 'medium')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product_image_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='assign.product_main_model')),
            ],
        ),
        migrations.CreateModel(
            name='Product_colour_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(choices=[('red', 'red'), ('green', 'green'), ('black', 'black'), ('blue', 'blue')], max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colour', to='assign.product_main_model')),
            ],
        ),
    ]