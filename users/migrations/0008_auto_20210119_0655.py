# Generated by Django 3.1.5 on 2021-01-19 06:55

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210119_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
