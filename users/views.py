from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User


from .models import Profile
from django import forms

from .utils import is_valid_password


# Create your views here.

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

def index(request):
    if not request.user.is_authenticated:
        return render(request,'users/index.html',{
            "not_authenticated":"Please log in to proceed."
        })
    
    else:
        if request.method=='POST':
            profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

            if profile_form.is_valid():
                profile_form.save()
                

    return render(request, "users/index.html",{
        "form":UpdateProfileForm(),
    })

def login_view(request):
    if request.method== "POST":   
        username= request.POST["username"]   
        password = request.POST["password"]   
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "users/index.html",{
                "message": "Logged in successfully!",
            })
        else:
            return render(request, "users/index.html" , {
            "message": "Invalid credentials.",
            "not_authenticated":"Please log in to proceed."
            })

    return render(request, "users/index.html")
     
def logout_view(request):
    logout(request)
    return render(request,'users/index.html',{
        "not_authenticated":"Please log in to proceed."
    }) 


def signup_view(request): 
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']   
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if username:
            if password1 == password2:
                if is_valid_password(password1):
                    user = User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                    user.save()
                    login(request, user)
                    return HttpResponseRedirect(reverse("users:index"))
                else:
                    return render(request,'users/index.html',{
                        "message":"Passwords must contain at least 8 characts including sympbols, lowercase, uppercase letters and numbers.",
                        "not_authenticated":"Please log in to proceed."
                    })
            else: 
                return render(request,'users/index.html',{
                    "message":"Passwords no match",       
                    "not_authenticated":"Please log in to proceed."            
                })
        else:
              
            return render(request,'users/index.html',{
                "message":"Did you forget to fill in your username?",
                "not_authenticated":"Please log in to proceed."
                
            })

      
    return render(request,'users/index.html',{

        
    })


def change_password_view(request):
    if request.method == 'POST':
        username=request.POST['username']
        password0=request.POST['password0']
        password1=request.POST['password1']
        password2=request.POST['password2']
        user = authenticate(request, username=username, password=password0)

        if user:
            if password1 == password2:
                if is_valid_password(password1):
                    user.set_password('password1')
                    user.save()
                    update_session_auth_hash(request, user) #delets the past sessions and start a new one
                    login(request, user)
                    return render(request, "users/index.html",{
                        "message": "Password changed successfully!",                 
                    })
  
            else:
                  
                return render(request, "users/index.html",{
                    "message": "Password didn't match!",
                   
                })
        else:
            return render(request, "users/index.html",{
                "message": "Incorrect user name or old password or both!",               
            })    