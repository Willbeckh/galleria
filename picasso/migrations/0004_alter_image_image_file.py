# Generated by Django 4.0.4 on 2022-05-27 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picasso', '0003_rename_img_description_image_image_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(upload_to='picasso/images/'),
        ),
    ]