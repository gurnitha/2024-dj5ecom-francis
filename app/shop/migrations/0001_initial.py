# Generated by Django 5.0.1 on 2024-01-09 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=120)),
                ('slug', models.SlugField(max_length=255)),
                ('image', models.ImageField(upload_to='category_images/%Y/%m/%d/')),
                ('is_mega', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=120)),
                ('button_text', models.CharField(max_length=60)),
                ('button_link', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='sliders/%Y/%m/%d/')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=120)),
                ('button_text', models.CharField(max_length=60)),
                ('button_link', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='sliders/%Y/%m/%d/')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.CharField(max_length=120)),
                ('more_description', models.TextField(blank=True, null=True)),
                ('additional_infos', models.TextField(blank=True, null=True)),
                ('stock', models.IntegerField()),
                ('solde_price', models.IntegerField()),
                ('regular_price', models.IntegerField()),
                ('brand', models.CharField(blank=True, max_length=60, null=True)),
                ('is_available', models.BooleanField()),
                ('is_best_seller', models.BooleanField()),
                ('is_new_arrival', models.BooleanField()),
                ('is_featured', models.BooleanField()),
                ('is_special_offer', models.BooleanField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/%Y/%m/%d/')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.product')),
            ],
        ),
    ]
