from os import access
from django.db import models

# Create your models here.
class Alumnis(models.Model):
  fname = models.CharField(max_length=255,default="")
  lname = models.CharField(max_length=255,default="")
  email = models.CharField(max_length=255)
  mobile = models.IntegerField(default=0)
  password = models.CharField(max_length=255)
  otp = models.IntegerField(default=0)
  verified = models.IntegerField(default=0)

class Faculty(models.Model):
  fname = models.CharField(max_length=255,default="")
  lname = models.CharField(max_length=255,default="")
  email = models.CharField(max_length=255)
  mobile = models.IntegerField(default=0)
  password = models.CharField(max_length=255)
  access = models.IntegerField(default=0)