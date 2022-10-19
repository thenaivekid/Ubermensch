import random
import datetime
from email.quoprimime import quote
from urllib import response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone,timesince
from .forms import EmailForm

from django.core.mail import send_mail

from .models import Quotes, SelfRealizations,Timespent,BiggestGoals,Values,Fears,PersonalityTraits,Likes,Dislikes,Strengths,Weaknesses,FindingLove,Romances,DosAndDonts,GoldenRules,TraitsUpgrading,WatchList,ReadingList,SkillList


# Create your views here.

def home(request):
    user = request.user
    if not user:
        return HttpResponse("Please login to proceed.")
    quotes =Quotes.objects.all()
    quote= random.choice(quotes)
    if request.method=='POST':
        formname= request.POST['formname']
        
        if formname=='quote':
            new_quote = request.POST["new_quote"]
            new_saidby= request.POST["new_saidby"]
            Quotes.objects.create(quote=new_quote,saidby=new_saidby)
            return HttpResponseRedirect(reverse('home'))

        if formname=='goal':
            goal = request.POST["goal"]
            BiggestGoals.objects.create(user=user,goal=goal)
            return HttpResponseRedirect(reverse('home'))

        if formname=='goal':
            goal = request.POST["goal"]
            BiggestGoals.objects.create(user=user,goal=goal)
            return HttpResponseRedirect(reverse('home'))
    return render(request, "DeepDive/home.html",{
        "quote": quote,
        "goals": BiggestGoals.objects.filter(user=user).all(),
    })

def about(request):
    return render(request, "DeepDive/about.html")

def knowthyself(request):
    user = request.user
    if request.method =='POST':
        
        if request.POST['formname']=='value':
            Values.objects.create(user=user,value=request.POST['value'])
        if request.POST['formname']=='fear':
            Fears.objects.create(user=user,fear=request.POST['fear'])
        if request.POST['formname']=='personality_trait':
            PersonalityTraits.objects.create(user=user,openness=request.POST['openness_score'],conscientiousness=request.POST['conscientiousness_score'],extroversion=request.POST['extroversion_score'],agreeableness=request.POST['agreeableness_score'],neuroticism=request.POST['neuroticism_score'])
        if request.POST['formname']=='like':
            Likes.objects.create(user=user,like=request.POST['like'])
        if request.POST['formname']=='dislike':
            Dislikes.objects.create(user=user,dislike=request.POST['dislike'])
        if request.POST['formname']=='strength':
            Strengths.objects.create(user=user,strength=request.POST['strength'])
        if request.POST['formname']=='weakness':
            Weaknesses.objects.create(user=user,weakness=request.POST['weakness'])
        if request.POST['formname']=='self_realization':
            SelfRealizations.objects.create(user=user,selfrealization=request.POST['self_realization'])
    return render(request, "DeepDive/knowthyself.html",{
        "fears":Fears.objects.filter(user=user).all(),
        "values":Values.objects.filter(user=user).all(),
        "personality_traits":PersonalityTraits.objects.filter(user=user).all(),
        "likes":Likes.objects.filter(user=user).all(),
        "dislikes":Dislikes.objects.filter(user=user).all(),
        "strengths":Strengths.objects.filter(user=user).all(),
        "weaknesses":Weaknesses.objects.filter(user=user).all(),
        "self_realizations":SelfRealizations.objects.filter(user=user).all(),
    })

def overcomethyself(request):
    user= request.user
    if request.method =='POST':
        if request.POST['formname']=='trait':
            TraitsUpgrading.objects.create(user=user,trait=request.POST['trait'])

    return render(request, "DeepDive/overcomethyself.html",{
        'traits':TraitsUpgrading.objects.filter(user=user).all(),
    })

def love(request):
    user=request.user
    if request.method=='POST':
        if request.POST['formname']=='thought':
            FindingLove.objects.create(user=user,thought=request.POST['thought'])
        if request.POST['formname']=='romance':
            Romances.objects.create(user=user,romance=request.POST['romance'])
        if request.POST['formname']=='point':
            DosAndDonts.objects.create(user=user,point=request.POST['point'])
        if request.POST['formname']=='rule':
            GoldenRules.objects.create(user=user,rule=request.POST['rule'])
    return render(request, "DeepDive/love.html",{
        "thoughts":FindingLove.objects.filter(user=user).all(),
        "romances":Romances.objects.filter(user=user).all(),
        "points":DosAndDonts.objects.filter(user=user).all(),
        "rules":GoldenRules.objects.filter(user=user).all(),
    })

def spinningwheels(request):
    return render(request, "DeepDive/spinningwheels.html")

def activities(request):
    user=request.user
    if request.method =='POST':
        if request.POST['formname']=='watched_movie':
            movie=WatchList.objects.get(user=user,id=request.POST['movie_id']) 
            movie.finished_watching=True
            movie.save()
        if request.POST['formname']=='read_book':
            book=ReadingList.objects.get(user=user,id=request.POST['book_id']) 
            book.finished_reading=True
            book.save()
        if request.POST['formname']=='learnt_skill':
            skill=SkillList.objects.get(user=user,id=request.POST['skill_id']) 
            skill.finished_learning=True
            skill.save()
        if request.POST['formname']=='movie':
            WatchList.objects.create(user=user,show=request.POST['movie']) 
        if request.POST['formname']=='book':
            ReadingList.objects.create(user=user,book=request.POST['book'])
        if request.POST['formname']=='skill':
            SkillList.objects.create(user=user,skill=request.POST['skill'])
    return render(request, "DeepDive/activities.html",{
        'movies':WatchList.objects.filter(user=user,finished_watching=False).all(),
        'watched_movies':WatchList.objects.filter(user=user,finished_watching=True).all(),
        'books':ReadingList.objects.filter(user=user,finished_reading=False).all(),
        'read_books':ReadingList.objects.filter(user=user,finished_reading=True).all(),
        'skills':SkillList.objects.filter(user=user,finished_learning=False).all(),
        'learnt_skills':SkillList.objects.filter(user=user,finished_learning=True).all(),
    })


def user(request):
    return HttpResponseRedirect(reverse("users:index"))

def emptiness(request):
    return render(request, "DeepDive/emptiness.html")

def contact(request):
    if request.method =='POST':
        form= EmailForm(request.POST)
        if form.is_valid():
            sentfrom=request.user.email
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

def journal(request):
    return HttpResponseRedirect(reverse("journal:index"))

def timespent(request):
    timespent = request.POST['timespent']
    response = timespent
    Timespent.objects.create(timespent=timespent)
    return HttpResponse(response)