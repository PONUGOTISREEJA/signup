from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registration(request):
    if request.method == 'POST':
        uusername=request.POST.get('name')
        umail=request.POST.get('email')
        upassword=request.POST.get('password')
        uconfirmpassword=request.POST.get('confirmpassword')
        if upassword!=uconfirmpassword:
            return HttpResponse("Password and ConfirmPassword are not Matching")
        else:
            user_registration=User.objects.create_user(uusername,umail,upassword)
            user_registration.save()
            return redirect(login1)
        

    return render(request,"registration.html")

def login1(request):
    if request.method=='POST':
        uusername=request.POST.get("name")
        upassword=request.POST.get("password")
        authenticate_user=authenticate(request,username=uusername,password=upassword)
        if authenticate_user  is not None:

            login(request,authenticate_user)
            return redirect(home)
        else:
            return HttpResponse("invalid user")
            
    return render (request,'login.html')

@login_required(login_url="login")
def home(request):
    

    return render(request,"home.html")


def logout1(request):
    logout(request)
    return redirect(login1)