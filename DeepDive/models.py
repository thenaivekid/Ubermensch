from email.policy import default
from email.quoprimime import quote
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quotes(models.Model):
    quote = models.CharField(max_length=128)
    saidby = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.quote} -{self.saidby}"

class Timespent(models.Model):
    timespent = models.DateTimeField()

    def __str__(self):
        return f"{self.timespent}"

class UserInputs(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)

class BiggestGoals(UserInputs):
    goal = models.CharField(max_length=64)

class Values(UserInputs):
    value =models.CharField(max_length=32)

class Fears(UserInputs):
    fear =models.CharField(max_length=32)

class Values(UserInputs):
    value =models.CharField(max_length=32)

class PersonalityTraits(UserInputs):
    openess =models.IntegerField(default=0)
    conscientiousness =models.IntegerField(default=0)
    extroversion =models.IntegerField(default=0)
    agreableness =models.IntegerField(default=0)
    neuroticism =models.IntegerField(default=0)

class Likes(UserInputs):
    like =models.CharField(max_length=32)

class Dislikes(UserInputs):
    dislike =models.CharField(max_length=32)

class Strengths(UserInputs):
    strength =models.CharField(max_length=32)

class Weaknesses(UserInputs):
    weakness =models.CharField(max_length=32)

class SelfRealizations(UserInputs):
    selfrealization =models.CharField(max_length=32)