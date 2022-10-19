from email.policy import default
from email.quoprimime import quote
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Timespent(models.Model):
    timespent = models.DateTimeField()

    def __str__(self):
        return f"{self.timespent}"

class UserInputs(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)

#for home
class Quotes(models.Model):
    quote = models.CharField(max_length=128)
    saidby = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.quote} -{self.saidby}"



class BiggestGoals(UserInputs):
    goal = models.CharField(max_length=64)

#for knowthyself
class Values(UserInputs):
    value =models.CharField(max_length=32)

class Fears(UserInputs):
    fear =models.CharField(max_length=32)



class PersonalityTraits(UserInputs):
    openness =models.IntegerField(default=0)
    conscientiousness =models.IntegerField(default=0)
    extroversion =models.IntegerField(default=0)
    agreeableness =models.IntegerField(default=0)
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

#for overcomingthyself

class TraitsUpgrading(UserInputs):
    trait =models.CharField(max_length=32) 
    
# class Meditions(UserInputs):
#     meditation =models.CharField(max_length=32)

# class Exercises(UserInputs):
#     exercise =models.CharField(max_length=32) 


# class CharismaTips(UserInputs):
#     tip =models.CharField(max_length=32) 

# class LeadershipTips(UserInputs):
#     leading_tip =models.CharField(max_length=32) 

# class Comrades(UserInputs):
#     name =models.CharField(max_length=32) 
#     service= models.CharField(max_length=32) 

# class ObservationStratedy(UserInputs):
#     stratedy =models.CharField(max_length=128)

#for love
class FindingLove(UserInputs):
    thought =models.CharField(max_length=32)

class Romances(UserInputs):
    romance =models.CharField(max_length=32)

class DosAndDonts(UserInputs):
    point =models.CharField(max_length=32)

class GoldenRules(UserInputs):
    rule =models.CharField(max_length=32)

#for spinningwheels
# class ThemesOfTheDay(models.Model):
#     theme= models.CharField(max_length=32)

# class SocialDare(models.Model):
#     dare= models.CharField(max_length=32)

# class CharacterTraits(models.Model):
#     charactertrait= models.CharField(max_length=32)

# class Emotions(models.Model):
#     emotion= models.CharField(max_length=32)

# class Visualizatoins(models.Model):
#     visualization= models.CharField(max_length=32)

#for activity
class WatchList(UserInputs):
    show= models.CharField(max_length=32)
    finished_watching = models.BooleanField(default=False)

class ReadingList(UserInputs):
    book= models.CharField(max_length=32)
    finished_reading = models.BooleanField(default=False)
    
class SkillList(UserInputs):
    skill= models.CharField(max_length=32)
    finished_learning = models.BooleanField(default=False)
    