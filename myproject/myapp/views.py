from django.shortcuts import redirect, render
from django.contrib.auth.models import *
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import *
# Create your views here.
def home(req):
    return render(req,"home.html")


def login(req):
    if req.method =='POST':
        username=req.POST.get("username")
        password=req.POST.get("password")

        if not User.objects.all().filter(username=username).exists():
            messages.info(req,"Incorrect User Name")
            redirect('/login/')
        else:
            user=authenticate(username=username,password=password)
            if user is None:
                messages.info(req,"Incorrect Password")
                redirect('/login/')
            else:
                queryset=movie.objects.all()
                return render(req,"menu.html",context={"movie":queryset})

    return render(req,"login.html")

def register(req):
    if req.method == "POST":
        username=req.POST.get("username")
        password=req.POST.get("password")

        queryset=User.objects.create_user(
            username=username
        )
        queryset.set_password(password)
        queryset.save()
        messages.info(req,"Account Created Successfully")
        
    return render(req,"register.html")
