# Generated by Django 4.0.4 on 2022-05-30 21:17

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picasso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]