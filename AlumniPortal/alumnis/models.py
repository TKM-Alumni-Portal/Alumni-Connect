from os import access
from django.db import models
from traitlets import default

# Create your models here.
class Alumnis(models.Model):
  fname = models.CharField(max_length=255,default="")
  lname = models.CharField(max_length=255,default="")
  email = models.CharField(max_length=255,primary_key=True)
  branch = models.CharField(max_length=255,default="")
  yoa = models.IntegerField(default=0)
  mobile = models.IntegerField(default=0)
  password = models.CharField(max_length=255)
  otp = models.IntegerField(default=0)
  verified = models.IntegerField(default=0)
  profile = models.IntegerField(default=0)

class AlumniProfile(models.Model):
  email = models.CharField(max_length=255,primary_key=True)
  specialization = models.CharField(max_length=255,default="")
  linkedID = models.CharField(max_length=255,default="")
  industry = models.CharField(max_length=255,default="")
  position = models.CharField(max_length=255,default="")
  location = models.CharField(max_length=255,default="")
  gf = models.IntegerField(default=0)
  cs = models.IntegerField(default=0)
  fi = models.IntegerField(default=0)
  research = models.IntegerField(default=0)
  fdp = models.IntegerField(default=0)
  mdp = models.IntegerField(default=0)
  iv = models.IntegerField(default=0)
  buddySys = models.IntegerField(default=0)
  consulting = models.IntegerField(default=0)
  sip = models.IntegerField(default=0)
  placements = models.IntegerField(default=0)
  ic = models.IntegerField(default=0)
  lps = models.IntegerField(default=0)
  csr = models.IntegerField(default=0)
  ssp = models.IntegerField(default=0)
  se = models.IntegerField(default=0)


class Faculty(models.Model):
  fname = models.CharField(max_length=255,default="")
  lname = models.CharField(max_length=255,default="")
  email = models.CharField(max_length=255)
  mobile = models.IntegerField(default=0)
  password = models.CharField(max_length=255)
  access = models.IntegerField(default=0)

class AlumniProPic(models.Model):
  proPic = models.ImageField(upload_to='alumniProPic/')
  email = models.CharField(max_length=255,primary_key=True, default="")
  