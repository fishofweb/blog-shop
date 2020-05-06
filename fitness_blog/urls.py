# from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path("", views.home, name = "HOME"),
    path("blog_detail/<int:id>", views.blog_detail, name = "blog"),
    # path("about/", views.about, name="about"),
    # path("contact/", views.contact, name="contact"),
    path("back/", views.back1, name="back"),
    # re_path(r'^back/$', views.back1, name="back"),
    path("chest/", views.chest, name="chest"),
    path("shoulder/",views.shoulder, name="shoulder"),
    path("abs/", views.abs, name="abs"),
    path("bicep/", views.bicep, name="bicep"),
    path("tricep/", views.tricep, name= "tricep"),
    path("forearm/", views.forearm, name="forearm"),
    path("legs/", views.legs, name="legs"),
    path("fullbody/", views.fullbody, name="fullbody"),
    path("search/", views.search, name="search"),

]
