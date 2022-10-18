# Generated by Django 4.1 on 2022-08-12 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0003_rename_catagory_tb_category_tb_and_more'),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('stock', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to='')),
                ('details', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('categoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteadmin.category_tb')),
                ('sellerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.seller_tb')),
            ],
        ),
    ]
