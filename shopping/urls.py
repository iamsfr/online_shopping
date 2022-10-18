"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from siteadmin import views as adminview
from buyer import views as buyerview
from seller import views as sellerview
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',adminview.index,name='index'),
    path('login/',adminview.login,name='login'),
    path('loginAction/',adminview.loginAction,name='loginAction'),
    path('addcategory/',adminview.addcategory,name='addcategory'),
    path('addcategoryAction/',adminview.addcategoryAction,name='addcategoryAction'),
    path('buyerregistration/',buyerview.buyerregistration,name='buyerregistration'),
    path('registerAction/',buyerview.registerAction,name='registerAction'),
    path('checkusername/',adminview.checkusername,name='checkusername'),
    path('sellerregistration/',sellerview.sellerregistration,name='sellerregistration'),
    path('sellerAction/',sellerview.sellerAction,name='sellerAction'),
    path('checkusername/',adminview.checkusername,name='checkusername'),
    path('viewregisterd/',adminview.viewregisterd,name='viewregisterd'),
    path('approved/<int:id>',adminview.approved,name='approved'),
    path('reject/<int:id>',adminview.reject,name='reject'),
    path('sellerupdateprofile/',sellerview.sellerupdateprofile,name='sellerupdateprofile'),
    path('sellerupdateAction/',sellerview.sellerupdateAction,name='sellerupdateAction'),
    path('buyerupdateprofile/',buyerview.buyerupdateprofile,name='buyerupdateprofile'),
    path('buyerupdateAction/',buyerview.buyerupdateAction,name='buyerupdateAction'),
    path('addproduct/',sellerview.addproduct,name='addproduct'),
    path('addproductAction/',sellerview.addproductAction,name='addproductAction'),
    path('viewaddedproduct/',sellerview.viewaddedproduct,name='viewaddedproduct'),
    path('delete/<int:id>',sellerview.delete,name='delete'),
    path('edit/<int:id>',sellerview.edit,name='edit'),
    path('updateAction',sellerview.updateAction,name='updateAction'),
    path('buyerviewaddedproducts/',buyerview.buyerviewaddedproducts,name='buyerviewaddedproducts'),
    path('addtocart/<int:id>',buyerview.addtocart,name='addtocart'),
    path('cartAction/',buyerview.cartAction,name='cartAction'),
    path('viewcart/',buyerview.viewcart,name='viewcart'),
    path('deletecart/<int:id>',buyerview.deletecart,name='deletecart'),
    path('placeorderAction/',buyerview.placeorderAction,name='placeorderAction'),
    path('buyerviewaddedorders/',buyerview.buyerviewaddedorders,name='buyerviewaddedorders'),
    path('cancel/<int:id>',buyerview.cancel,name='cancel'),
    path('viewbuyerproduct/',sellerview.viewbuyerproduct,name='viewbuyerproduct'),
    path('orderapproved/<int:id>',sellerview.orderapproved,name='orderapproved'),
    path('orderreject/<int:id>',sellerview.orderreject,name='orderreject'),
    path('trackingid/<int:id>',sellerview.trackingid,name='trackingid'),
    path('trackingidAction/',sellerview.trackingidAction,name='trackingidAction'),
    path('confirmcancel/<int:id>',sellerview.confirmcancel,name='confirmcancel'),
    path('viewtrackingdetails<int:id>/',buyerview.viewtrackingdetails,name='viewtrackingdetails'),
    path('searchitem/',buyerview.searchitem,name='searchitem'),
    path('searchAction/',buyerview.searchAction,name='searchAction'),
    path('searchbycategory/',buyerview.searchbycategory,name='searchbycategory'),
    path('searchcategoryAction/',buyerview.searchcategoryAction,name='searchcategoryAction'),
    path('forgotpassword/',adminview.forgotpassword,name='forgotpassword'),
    path('forgotAction/',adminview.forgotAction,name='forgotAction'),
    path('newpasswordAction/',adminview.newpasswordAction,name='newpasswordAction'),
    path('enternewAction/',adminview.enternewAction,name='enternewAction'),
    path('logout/',adminview.logout,name='logout')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
