from django.shortcuts import render,redirect
from siteadmin.models import *
from buyer.models import *
from seller.models import *
from django.contrib import messages
from django.http import JsonResponse
import datetime


# Create your views here.
def buyerregistration(request):
    return render(request,"buyerregistration.html")

def registerAction(request):
    name=request.POST['name']
    address=request.POST['address']
    dob=request.POST['dob']
    gender=request.POST['gender']
    phonenumber=request.POST['phonenumber']
    country=request.POST['country']
    username=request.POST['username']
    password=request.POST['password']

    user=buyer_tb(name=name,address=address,dob=dob,gender=gender,phonenumber=phonenumber,
                  country=country,username=username,password=password)
    user.save()
    messages.add_message(request,messages.INFO,"registeration complete")
    return redirect('buyerregistration')


def buyerupdateprofile(request):
    buyerid=request.session['id']
    buyer=buyer_tb.objects.filter(id=buyerid)
    return render(request,"buyerupdateprofile.html",{'data':buyer})

def buyerupdateAction(request):
    buyerid=request.POST['id']
    buyer=buyer_tb.objects.filter(id=buyerid)
    name=request.POST['name']
    address=request.POST['address']
    dob=request.POST['dob']
    gender=request.POST['gender']
    phonenumber=request.POST['phonenumber']
    country=request.POST['country']
    username=request.POST['username']
    password=request.POST['password']

    buyer=buyer_tb.objects.filter(id=buyerid).update(name=name,address=address,dob=dob,
                                        gender=gender,phonenumber=phonenumber,country=country,username=username,password=password)
    messages.add_message(request,messages.INFO,"updation complete")
    return redirect('buyerupdateprofile')

def buyerviewaddedproducts(request):
    buyerid=request.session['id']
    buyer=product_tb.objects.all()
    return render(request,'buyerviewaddedproducts.html',{'data':buyer})
def addtocart(request,id):
    buyer=product_tb.objects.filter(id=id)
    return render(request,'addtocart.html',{'buyer':buyer})

def cartAction(request):
    buyerid=request.session['id']
    productid=request.POST['id']
    shipping=request.POST['shipping']
    quantity=request.POST['quantity']
    phone=request.POST['phone']
    totalprice=request.POST['totalprice']
    cart=cart_tb(buyerid_id=buyerid,productid_id=productid,shippingaddress=shipping,quantity=quantity,phone=phone,totalprice=totalprice)
    messages.add_message(request,messages.INFO,"Add to cart complete")
    cart.save()
    return redirect('buyerviewaddedproducts')
def viewcart(request):
    buyerid=request.session['id']
    cart=cart_tb.objects.filter(buyerid=buyerid)
    return render(request,'viewcart.html',{'cart':cart})
def deletecart(request,id):
    user=cart_tb.objects.filter(id=id).delete()
    return redirect('viewcart')

def placeorderAction(request):
    cartitems=request.POST.getlist('checkbox')
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    for cid in cartitems:
        cartitem=cart_tb.objects.filter(id=cid)
        stock=cartitem[0].productid.stock
        quantity=cartitem[0].quantity
        shipping=cartitem[0].shippingaddress
        phone=cartitem[0].phone
        totalprice=cartitem[0].totalprice
        sellerid=cartitem[0].productid.sellerid
        productid=cartitem[0].productid
        buyerid=cartitem[0].buyerid
        
        if quantity>int(stock):
            messages.add_message(request,messages.INFO,'Quantity is Greater')
            return redirect('viewcart')
        else:
            order=order_tb(quantity=quantity,shipping=shipping,phone=phone,totalprice=totalprice,buyerid=buyerid,productid=productid,sellerid=sellerid,date=date,time=time)
            order.save()
            messages.add_message(request,messages.INFO,'Add To Cart Success')
            stocknew=int(stock)-quantity
            product=product_tb.objects.filter(id=productid.id).update(stock=stocknew)
            cartitem.delete()
            messages.add_message(request,messages.INFO,'item update successfully')
            return redirect('viewcart')
        
    
def buyerviewaddedorders(request):
    buyerid=request.session['id']
    buyers=order_tb.objects.filter(buyerid=buyerid)
    return render(request,'buyerviewaddedorders.html',{'buyers':buyers})

def cancel(request,id):
    order=order_tb.objects.filter(id=id).update(status='cancel')
    return redirect('buyerviewaddedorders')

def viewtrackingdetails(request,id):
    #buyerid=request.session['id']
    buyersview=track_tb.objects.filter(id=id)
    return render(request,'viewtrackingdetails.html',{'buyersview':buyersview})
def searchitem(request):
    return render(request,'searchitem.html')
def searchAction(request):
    product_name=request.POST['product_name']
    product=product_tb.objects.filter(product_name__istartswith=product_name)
    return render(request,'buyerviewaddedproducts.html',{'data':product})

def searchbycategory(request):
    category=category_tb.objects.all()
    return render(request,'searchbycategory.html',{'category':category})

def searchcategoryAction(request):
    category=request.POST['category']
    price=request.POST['price']
    viewcategory=product_tb.objects.filter(price__lte=price,categoryid=category)
    return render(request,'buyerviewaddedproducts.html',{'data':viewcategory})
