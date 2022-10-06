from django.urls import path 
from . import views

urlpatterns = [ 
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("knowthyself/", views.knowthyself, name="knowthyself"),
    path("overcomethyself/", views.overcomethyself, name="overcomethyself"),
    path("love/", views.love, name="love"),
    path("spinningwheels/", views.spinningwheels, name="spinningwheels"),
    path("activities/", views.activities, name="activities"),
    path("journal/", views.journal, name="journal"),
    path("emptiness/", views.emptiness, name="emptiness"),
    
]