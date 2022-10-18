from django.db import models

# Create your models here.
class seller_tb(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    file=models.FileField()
    status=models.CharField(max_length=20,default='pending')
    
class product_tb(models.Model):
    product_name=models.CharField(max_length=20)
    stock=models.CharField(max_length=20)
    file=models.FileField()
    details=models.CharField(max_length=20)
    price=models.IntegerField()
    categoryid=models.ForeignKey('siteadmin.category_tb',on_delete=models.CASCADE)
    sellerid=models.ForeignKey('seller_tb',on_delete=models.CASCADE)
class track_tb(models.Model):
    orderid=models.ForeignKey('buyer.order_tb',on_delete=models.CASCADE)
    details=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
