from django.urls import path
from . import views
# from django.conf.urls import url
urlpatterns = [
    path("", views.home, name = "HOME"),
    path("cart",views.productpage,name= "productpagename"),
    path("newarrival", views.newarrivals, name="narrivals"),
    path("naproduct_detail/<int:id>", views.naproduct_detail, name = "nadetail"),
    path("wtproduct_detail/<int:id>", views.wtproduct_detail, name = "wtdetail"),
    path("wsproduct_detail/<int:id>", views.wsproduct_detail, name = "wsdetail"),
    path("msproduct_detail/<int:id>", views.msproduct_detail, name = "msdetail"),
    path("mtproduct_detail/<int:id>", views.mtproduct_detail, name = "mtdetail"),
    path("eqproduct_detail/<int:id>", views.eqproduct_detail, name = "eqdetail"),
    path("womentrouser", views.womentrousers, name="wtrousers"),
    path("mentrouser", views.mentrousers, name="mtrousers"),
    path("menshirt", views.menshirts, name="mshirts"),
    path("womenshirt", views.womenshirts, name="wshirts"),
    path("equipment", views.machine, name="machines"),
    path("contactus", views.contact, name= "ctus"),
    path("chectout", views.checkoutnow, name= "chout"),
    path("chectout-confirm", views.checkout, name="checkingout"),
    path("chectoutconfm", views.checkoutc, name="confirm-checkout"),
    path("searchthings", views.searchin, name= "searchweb"),
    ]
