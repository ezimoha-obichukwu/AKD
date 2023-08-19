from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def home_page(request):
    return render(request, "a.html")

def registration_page(request):
    if request.method == "POST":
        new_username = request.POST["username"]
        new_email = request.POST["email"]
        new_password = request.POST["password1"]
        new_password_2 = request.POST["password2"]

        if new_password == new_password_2:
            if User.objects.filter(username=new_username).exists():
                  messages.error(request, "User already exists")
                  return redirect("register")
            elif User.objects.filter(email=new_email).exists():
             messages.error(request, "User already exists")
             return redirect("register")
            else:
                User.objects.create_user(username=new_username, email=new_email, password=new_password)
                messages.success(request, "Your account has been created successfully")
                return redirect("login")
        else:
            messages.error(request, "Both passwords must match")
            return redirect("register")
    else:
        return render(request, "register.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        
        else:
            messages.error(request, "Invalid credentials supplied")
            return redirect("login")
        
    else:
        return render(request, "login.html")



def logout(request):
    auth.logout(request)
    return redirect("/")