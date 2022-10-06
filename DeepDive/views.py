from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "DeepDive/home.html")

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
    return render(request, "DeepDive/activities.html")

def journal(request):
    return render(request, "DeepDive/journal.html")

def user(request):
    return render(request, "DeepDive/user.html")

def emptiness(request):
    return render(request, "DeepDive/emptiness.html")