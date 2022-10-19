from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='images')
    bio = models.TextField()