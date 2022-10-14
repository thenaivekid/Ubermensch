from urllib import response
from django.test import TestCase
from django.test import Client,client
from django.urls import reverse

from .views import home
from .models import Quotes
# Create your tests here.
def create_quote(quote,saidby):
    return Quotes.objects.create(quote=quote,saidby=saidby)

class HomeViewTest(TestCase):
    def test_get_request(self):
        """displays home page for get request""" 
        create_quote(quote=" love",saidby="ashok")
        response= self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_add_quote_with_quote(self):
        """displays no qoute given in  home page for post request with no quote""" 
        create_quote(quote=" love",saidby="ashok")
        response=Client().post(reverse('home'),{'new_quote': "love",'new_saidby': "ashok"})
        self.assertEqual(response.status_code,302)

    def test_with_no_quote(self):
        """Returns home page with error message"""
        pass