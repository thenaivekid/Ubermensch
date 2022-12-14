from django.urls import path 
from . import views

urlpatterns = [ 
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("knowthyself/", views.knowthyself, name="knowthyself"),
    path("overcomethyself/", views.overcomethyself, name="overcomethyself"),
    path("love/", views.love, name="love"),
    path("spinningwheels/", views.spinningwheels, name="spinningwheels"),
    path("activities/", views.activities, name="activities"),
    path("emptiness/", views.emptiness, name="emptiness"),
    path("contact/", views.contact, name="contact"),
]