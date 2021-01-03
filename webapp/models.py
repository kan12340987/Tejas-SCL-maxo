from django.db import models
from django.contrib.auth.models import User as User_model
from django.core.validators import RegexValidator


# Create your models here.
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class Texbook(models.Model):
    Title = models.CharField(default = '', max_length=100)
    Author = models.CharField(default = '', max_length=50)
    Branch = models.CharField(default = '', max_length=50)
    Subject = models.CharField(default='', max_length=50)
    PublicationYear = models.IntegerField(default = 2021)
    link = models.URLField(default='')

class QPapers(models.Model):
    Branch = models.CharField(default = '', max_length=50)
    Subject = models.CharField(default='', max_length=50)
    year = models.IntegerField(default = 2021)
    Semester = models.IntegerField(default= 1)
    college = models.CharField(default = '', max_length=100)
    link = models.URLField(default='')

class notes(models.Model):
    Branch = models.CharField(default = '', max_length=50)
    Subject = models.CharField(default='', max_length=50)
    year = models.IntegerField(default = 2021)
    Semester = models.IntegerField(default= 1)
    college = models.CharField(default = '', max_length=50)   
    link = models.URLField(default='')