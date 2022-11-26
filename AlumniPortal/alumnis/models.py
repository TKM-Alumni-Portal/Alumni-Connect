from datetime import date,datetime
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
  proPic = models.ImageField(upload_to='FacultyProPic/',default="")
  penNumber = models.IntegerField(default=0)

class AlumniProPic(models.Model):
  proPic = models.ImageField(upload_to='alumniProPic/')
  email = models.CharField(max_length=255,primary_key=True, default="")

class Events(models.Model):
  name = models.CharField(max_length=255,primary_key=True)
  date = models.DateField()
  time = models.TimeField()
  description = models.CharField(max_length=1000, default="")
  mode = models.IntegerField(default=0)
  pic = models.ImageField(upload_to='events/', default="")
  status = models.IntegerField(default=0)

class Feedbacks(models.Model):
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  subject = models.CharField(max_length=500)
  message = models.CharField(max_length=1500)
  status = models.IntegerField(default=1)
  date = models.DateField(default=date.today())

class Gallery(models.Model):
  eventName = models.CharField(max_length=300)
  pic = models.ImageField(upload_to='gallery/')
  email = models.CharField(max_length=300)
  status = models.IntegerField(default=0)

class Post(models.Model):
  pid = models.AutoField(auto_created = True,primary_key = True)
  email = models.CharField(max_length=255)
  pname = models.CharField(max_length=300)
  description = models.CharField(max_length=1000, default="")
  timestamp = models.DateTimeField(default=datetime.now())