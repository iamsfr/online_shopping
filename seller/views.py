from django.shortcuts import render,redirect
from siteadmin.models import *
from seller.models import *
from buyer.models import *
from django.contrib import messages
from django.http import JsonResponse
import datetime


# Create your views here.
def sellerregistration(request):
    return render(request,'sellerregistration.html')

def sellerAction(request):
    name=request.POST['name']
    address=request.POST['address']
    dob=request.POST['dob']
    gender=request.POST['gender']
    country=request.POST['country']
    username=request.POST['username']
    password=request.POST['password']
    if len(request.FILES)>0:
        file=request.FILES['file']
    else:
        file="no pic"
    user=seller_tb(name=name,address=address,dob=dob,gender=gender,
                   country=country,username=username,password=password,file=file)
    user.save()
    messages.add_message(request,messages.INFO,"Register complete")
    return redirect('sellerregistration')

def sellerupdateprofile(request):
    sellerid=request.session['id']
    seller=seller_tb.objects.filter(id=sellerid)
    return render(request,"sellerupdateprofile.html",{'data':seller})

def sellerupdateAction(request):
    sellerid=request.POST['id']
    seller=seller_tb.objects.filter(id=sellerid)
    name=request.POST['name']
    address=request.POST['address']
    dob=request.POST['dob']
    gender=request.POST['gender']
    country=request.POST['country']
    username=request.POST['username']
    password=request.POST['password']
    if len(request.FILES)>0:
        file=request.FILES['file']
    else:
        file=seller[0].file
    seller_object=seller_tb.objects.get(id=sellerid)
    seller_object.file=file
    seller_object.save()
    seller=seller_tb.objects.filter(id=sellerid).update(name=name,address=address,dob=dob,gender=gender,country=country,username=username,password=password)
    messages.add_message(request,messages.INFO,"Seller Update complete")
    return redirect('sellerupdateprofile')
def addproduct(request):
    category=category_tb.objects.all()
    return render(request,'addproduct.html',{'data':category})
def addproductAction(request):
    productname=request.POST['productname']
    stock=request.POST['stock']
    details=request.POST['details']
    price=request.POST['price']
    categoryid=request.POST['categoryid']
    sellerid=request.session['id']
    if len(request.FILES)>0:
        file=request.FILES['file']
    else:
        file="no pic"  
    user=product_tb(product_name=productname,stock=stock,file=file,details=details,price=price,categoryid_id=categoryid,sellerid_id=sellerid)
    user.save()
    messages.add_message(request,messages.INFO,"product details completed")
    return redirect("addproduct")
    

def viewaddedproduct(request):
    sellerid=request.session['id']
    seller=product_tb.objects.filter(sellerid=sellerid)
    return render(request,'viewaddedproduct.html',{'data':seller})
def delete(request,id):
    viewer=product_tb.objects.filter(id=id).delete()
    return redirect('viewaddedproduct')
def edit(request,id):
    viewer=product_tb.objects.filter(id=id)
    category=category_tb.objects.all()
    return render(request,'selleredit.html',{'viewer':viewer,'data':category})

def updateAction(request):
    sellerid=request.session['id']
    productid=request.POST['id']
    product=product_tb.objects.filter(id=productid)
    productname=request.POST['productname']
    stock=request.POST['stock']
    details=request.POST['details']
    price=request.POST['price']
    categoryid=request.POST['categoryname']
    if len(request.FILES)>0:
        file=request.FILES['file']
    else:
        file=product[0].file
    product_object=product_tb.objects.get(id=productid)
    product_object.file=file
    product_object.save()
    seller=product_tb.objects.filter(id=productid).update(product_name=productname,stock=stock,details=details,price=price,categoryid_id=categoryid,file=file)
    messages.add_message(request,messages.INFO,"Edit complete")
    return redirect('viewaddedproduct')

def viewbuyerproduct(request):
    sellerid=request.session['id']
    orderview=order_tb.objects.filter(sellerid=sellerid)
    return render(request,'viewbuyerproduct.html',{'orderview':orderview})
def orderapproved(request,id):
    approve=order_tb.objects.filter(id=id).update(status='approved')
    return redirect('viewbuyerproduct')

def orderreject(request,id):
    orderreject=order_tb.objects.filter(id=id).update(status='reject')
    return redirect('viewbuyerproduct')
def trackingid(request,id):
    tracking=order_tb.objects.filter(id=id)
    return render(request,'trackingid.html',{'tracking':tracking})
def trackingidAction(request):
    orderid=request.POST['id']
    ordert=order_tb.objects.get(id=orderid)
    details=request.POST['details']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')  
    tracking=track_tb(orderid=ordert,date=date,time=time,details=details)
    tracking.save()
    return redirect('viewbuyerproduct')
def confirmcancel(request,id):
    confirmcancel=order_tb.objects.filter(id=id)
    confirmcancel.update(status='confirmcancel')
    quantity=confirmcancel[0].quantity
    stock=confirmcancel[0].productid.stock
    stock=int(stock)+quantity
    product=product_tb.objects.filter(id=confirmcancel[0].productid.id)
    product.update(stock=stock)
    return redirect('viewbuyerproduct')
    

    
    

