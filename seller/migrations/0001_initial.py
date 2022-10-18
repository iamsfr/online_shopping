# Generated by Django 4.0.6 on 2022-08-09 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='seller_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to='')),
                ('status', models.CharField(default='pending', max_length=20)),
            ],
        ),
    ]
