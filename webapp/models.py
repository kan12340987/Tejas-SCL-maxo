from django.db import models
from django.contrib.auth.models import User as User_model
from django.core.validators import RegexValidator


# Create your models here.
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class Texbook(models.Model):
    Title = models.TextField(default = '', max_length=100)
    Author = models.TextField(default = '', max_length=100)
    Branch = models.TextField(default = '', max_length=100)
    Subject = models.TextField(default='', max_length=100)
    PublicationYear = models.IntegerField(default = 2021)
    link = models.URLField(default='')

class QPapers(models.Model):
    Branch = models.TextField(default = '', max_length=100)
    Subject = models.TextField(default='', max_length=100)
    year = models.IntegerField(default = 2021)
    Semester = models.IntegerField(default= 1)
    college = models.TextField(default = '', max_length=100)
    link = models.URLField(default='')

class notes(models.Model):
    Branch = models.TextField(default = '', max_length=100)
    Subject = models.TextField(default='', max_length=100)
    year = models.IntegerField(default = 2021)
    Semester = models.IntegerField(default= 1)
    college = models.TextField(default = '', max_length=100)   
    link = models.URLField(default='')