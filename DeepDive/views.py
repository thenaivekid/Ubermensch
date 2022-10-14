import random
import datetime
from email.quoprimime import quote
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone,timesince
from .forms import EmailForm
from .models import Quotes
from django.core.mail import send_mail




# Create your views here.

def home(request):
    quotes =Quotes.objects.all()
    quote= random.choice(quotes)
    if request.method=='POST':
        new_quote = request.POST["new_quote"]
        new_saidby= request.POST["new_saidby"]
        if not new_quote:
            return render(request,"DeepDive/home.html",{
                "no_quote_given":"Please enter a quote.",
                "quote":quote
            })
        Quotes.objects.create(quote=new_quote,saidby=new_saidby)
        return HttpResponseRedirect(reverse('home'))
    
    return render(request, "DeepDive/home.html",{
        "quote": quote
    })

def about(request):
    return render(request, "DeepDive/about.html")

def knowthyself(request):
    return render(request, "DeepDive/knowthyself.html")

def overcomethyself(request):
    return render(request, "DeepDive/overcomethyself.html")

def love(request):
    return render(request, "DeepDive/love.html")

def spinningwheels(request):
    return render(request, "DeepDive/spinningwheels.html")

def activities(request):
    return render(request, "DeepDive/activities.html",{
    })

def journal(request):
    return render(request, "DeepDive/journal.html",{
    })

def user(request):
    return render(request, "DeepDive/user.html")

def emptiness(request):
    return render(request, "DeepDive/emptiness.html")

def contact(request):
    if request.method =='POST':
        form= EmailForm(request.POST)
        if form.is_valid():
            sentfrom=form.cleaned_data.get('sentfrom')
            subject = form.cleaned_data.get('subject')
            content = form.cleaned_data.get('content')
            send_mail(
                subject=subject,
                message=content,
                from_email=sentfrom,
                recipient_list=['neupane.ashok.9696@gmail.com'],
                fail_silently=False,
                )
        return HttpResponseRedirect(reverse('home'))

    return render(request,'deepdive/contact.html',{
        "form": EmailForm(),
    })