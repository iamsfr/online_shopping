# Generated by Django 4.1 on 2022-08-22 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_track_tb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_tb',
            name='price',
            field=models.IntegerField(),
        ),
    ]
