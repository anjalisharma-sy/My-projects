from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    summary= models.TextField(max_length=2000)
    education = models.CharField(max_length=200)
    
    work_experience = models.TextField(max_length=2000)
    projects = models.TextField(max_length=2000)
    skills= models.TextField(max_length=2000)