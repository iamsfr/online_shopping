from django.db import models

# Create your models here.
class buyer_tb(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    phonenumber=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class cart_tb(models.Model):
    buyerid=models.ForeignKey('buyer_tb',on_delete=models.CASCADE)
    productid=models.ForeignKey('seller.product_tb',on_delete=models.CASCADE)
    shippingaddress=models.CharField(max_length=20)
    quantity=models.IntegerField()
    phone=models.CharField(max_length=20)
    totalprice=models.IntegerField()

class order_tb(models.Model):
    sellerid=models.ForeignKey('seller.seller_tb',on_delete=models.CASCADE)
    productid=models.ForeignKey('seller.product_tb',on_delete=models.CASCADE)
    buyerid=models.ForeignKey('buyer_tb',on_delete=models.CASCADE)
    shipping=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    quantity=models.IntegerField()
    totalprice=models.IntegerField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='pending')
    
