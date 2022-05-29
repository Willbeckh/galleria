# Generated by Django 4.0.4 on 2022-05-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picasso', '0004_alter_image_image_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='categories',
            field=models.ManyToManyField(to='picasso.category'),
        ),
    ]
