from django import views
from django.urls import path

from . import views

app_name= 'journal'
urlpatterns= [ 
    path('',views.index,name="index"),
    path('newjournal/',views.newjournal,name="newjournal"),
    path('readjournal/<str:entry_name>/',views.readjournal,name="readjournal"),
    path('randomjournal/',views.randomjournal,name="randomjournal"),
    path('search/',views.search,name="search"),
]