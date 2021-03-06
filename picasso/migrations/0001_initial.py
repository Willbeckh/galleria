# Generated by Django 4.0.4 on 2022-05-29 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_tag', models.CharField(blank=True, default='Mars', max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='picasso/images/')),
                ('image_name', models.CharField(max_length=100)),
                ('image_description', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('categories', models.ManyToManyField(to='picasso.category')),
                ('image_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='picasso.location')),
            ],
        ),
    ]
