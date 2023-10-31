from operator import mod
from tkinter.ttk import Separator
from turtle import title
from unicodedata import name
from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=150, default="page")
    name = models.CharField(max_length=150)
    separator = models.CharField(max_length=10)
    description= models.TextField(max_length=250)


class Ring(models.Model):
    name = models.CharField(max_length=150)
    description= models.TextField(max_length=250)


class Cat(models.Model):
    name = models.CharField(max_length=150)
    description= models.TextField(max_length=250)

    
