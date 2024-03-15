# Generated by Django 5.0.1 on 2024-01-08 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
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
    ]
