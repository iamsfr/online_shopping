from django.shortcuts import render,redirect
from siteadmin.models import *
from django.contrib import messages
from buyer.models import *
from seller.models import *
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    admin=admin_tb.objects.filter(username=username,password=password)
    buyer=buyer_tb.objects.filter(username=username,password=password)
    seller=seller_tb.objects.filter(username=username,password=password)
    if admin.count()>0:
        request.session['id']=admin[0].id
        return render(request,"home.html",{'data':admin})
    elif buyer.count()>0:
        request.session['id']=buyer[0].id
        return render(request,"buyerhome.html",{'data':buyer})
    elif seller.count()>0:
        status=seller[0].status
        if status=="approved":
            request.session['id']=seller[0].id
            return render(request,"sellerhome.html",{'data':seller})
        else:
            messages.add_message(request,messages.INFO,"waiting for approvel")
            return redirect('login')
    else:
         messages.add_message(request,messages.INFO,"incorrect username")
         return redirect('login')
    
def addcategory(request):
    return render(request,'addcategory.html')
def addcategoryAction(request):
    name=request.POST['name']
    cname=category_tb(category_name=name)
    cname.save()
    messages.add_message(request,messages.INFO,"category name added")
    return redirect('addcategory')

def checkusername(request):
    username=request.GET['username']
    user=buyer_tb.objects.filter(username=username)
    if len(user)>0:
        msg="exist"
    else:
        msg="not exist"
    return JsonResponse({'valid':msg})

def viewregisterd(request):
    admin=request.session['id']
    seller=seller_tb.objects.all()
    return render(request,'viewregisterd.html',{'data':seller})
def approved(request,id):
    seller=seller_tb.objects.filter(id=id).update(status="approved")
    messages.add_message(request,messages.INFO,"Approved")
    return redirect('viewregisterd')
def reject(request,id):
    seller=seller_tb.objects.filter(id=id).update(status="reject")
    messages.add_message(request,messages.INFO,"Rejected")
    return redirect('viewregisterd')

def forgotpassword(request):
    return render(request,'forgotpassword.html')
def forgotAction(request):
    username=request.POST['username']
    sellerusername=seller_tb.objects.filter(username=username)
    buyerusername=buyer_tb.objects.filter(username=username)
    if sellerusername.count()>0:
        return render(request,'newpassword.html',{'user':username})
    elif buyerusername.count()>0:
        return render(request,'newpassword.html',{'user':username})
    else:
        messages.add_message(request,messages.INFO,"Incorrect username or password")
        return redirect('index')
def newpasswordAction(request):
    username=request.POST['username']
    name=request.POST['name']
    dob=request.POST['dob']
    country=request.POST['country']
    sellerp=seller_tb.objects.filter(username=username,name=name,dob=dob,country=country)
    buyerp=buyer_tb.objects.filter(username=username,name=name,dob=dob,country=country)
    if sellerp.count()>0:
        return render(request,'enternewpassword.html',{'user':username})
    elif buyerp.count()>0:
        return render(request,'enternewpassword.html',{'user':username})
    else:
        messages.add_message(request,messages.INFO,"message")
        return redirect('login')

def enternewAction(request):
    username=request.POST['username']
    npassword=request.POST['password']
    cpassword=request.POST['confirmpassword']
    seller=seller_tb.objects.filter(username=username)
    buyer=buyer_tb.objects.filter(username=username)
    if npassword==cpassword:
        if seller.count()>0:
            request.session['id']=seller[0].id
            sellerid=request.session['id']
            seller=seller_tb.objects.filter(id=sellerid).update(password=npassword)
        else:
            request.session['id']=buyer[0].id
            buyerid=request.session['id']
            buyer=buyer_tb.objects.filter(id=buyerid).update(password=npassword)
        messages.add_message(request,messages.INFO,"password changed succussfuly")
        request.session.flush()
        return redirect('index')
    else:
        messages.add_message(request,messages.INFO,"password mismatch")
        return render(request,'enternewpassword.html',{'user':username})

def logout(request):
    request.session.flush()
    messages.add_message(request,messages.INFO,"Logout success")
    return redirect('index')
    
