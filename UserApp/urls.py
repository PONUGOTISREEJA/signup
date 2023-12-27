from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    
    path("",views.registration,name="reg"),
    path("login/",views.login1,name="login"),
    path("home/",views.home,name="home"),
    path("logout/",views.logout1,name="logout"),



    
]
