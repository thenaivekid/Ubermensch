from email import message
import http
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User 
from django.contrib.auth.password_validation import validate_password,password_changed,password_validators_help_text_html

# Create your views here.

# to change the header of admin page



def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    else:
        help_texts = password_validators_help_text_html(password_validators=None)   
        return render(request, "users/user.html",{
            "help_texts": help_texts,
        })

def login_view(request):
    if request.method== "POST":   
        username= request.POST["username"]   
        password = request.POST["password"]   
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "users/user.html",{
                "message": "Logged in successfully!"
            })
        else:
            return render(request, "users/login.html" , {
            "message": "Invalid credentials."
            })

    return render(request, "users/login.html")
     
def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out"
    })


def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        validate_password(password, user=username, password_validators=None)
        user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
        user.save()
        login(request, user)
        return render(request, "users/user.html")

    help_texts = password_validators_help_text_html(password_validators=None)   
    return render(request,'users/signup.html',{
        "help_text": help_texts,
        
    })


def change_password_view(request):
    if request.method == 'POST':
        username=request.POST['username']
        password0=request.POST['password0']
        password1=request.POST['password1']
        password2=request.POST['password2']
        user = authenticate(request, username=username, password=password0)

        if user is not None:
            if password1 == password2:
                validate_password(password1, user=username, password_validators=None)
                user.set_password('password1')
                user.save()
                password_changed(password0, user=None, password_validators=None)
                login(request, user)
                return render(request, "users/user.html",{
                    "message": "Password changed successfully!",
                    "help_texts": help_texts,

                })
  
            else:
                help_texts = password_validators_help_text_html(password_validators=None)   
                return render(request, "users/user.html",{
                    "message": "Password didn't match!",
                    "help_texts": help_texts,
                })
        else:
            return render(request, "users/user.html",{
                "message": "Incorrect old password",
                "help_texts": help_texts,
            })    