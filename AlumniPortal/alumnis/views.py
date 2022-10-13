from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Alumnis
import random

from django.conf import settings
from django.core.mail import send_mail

def index(request):
  ouralumnis = Alumnis.objects.all().values()
  template = loader.get_template('test.html')
  context = {
    'ouralumnis': ouralumnis,
  }
  return HttpResponse(template.render(context, request))
  
def alumniReg(request):
  template = loader.get_template('alumniReg.html')
  return HttpResponse(template.render({}, request))

def addUser(request):
  x = request.POST['mail']
  y = request.POST['psw']
  mydata = Alumnis.objects.all()
  for i in mydata:
    if i.email==x:
      return HttpResponse("Email Id Already Exist!")
    else:
      a = Alumnis(email=x, password=y)
      a.save()
      num = random.randint(100000,999999)
      subject = 'Welcome to Alumni-Connect'
      message = f'Hi AJIL, Thank you for Joining in Alumni-Connect.'
      email_from = settings.EMAIL_HOST_USER
      recipient_list = [x, ]
      send_mail( subject, message, email_from, recipient_list )
      subject = 'Verify Your Account'
      message = f'Hi AJIL, '+str(num)+f' is Your One Time Password for account verification.'
      email_from = settings.EMAIL_HOST_USER
      recipient_list = [x, ]
      send_mail( subject, message, email_from, recipient_list )
      return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  a = Alumnis.objects.get(id=id)
  a.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  a = Alumnis.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'myalumnis': a,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  mail = request.POST['mail']
  psw = request.POST['psw']
  al = Alumnis.objects.get(id=id)
  al.email = mail
  al.password = psw
  al.save()
  return HttpResponseRedirect(reverse('index'))

def alumniSignIn(request):
  template = loader.get_template('alumniSignIn.html')
  return HttpResponse(template.render({}, request))

def alumniSignOut(request):
  template = loader.get_template('alumniSignIn.html')
  return HttpResponse(template.render({}, request))
  

def authAlumni(request):
  x = request.POST['mail']
  y = request.POST['psw']
  mydata = Alumnis.objects.all()
  for i in mydata:
    if i.email==x and i.password==y:
      request.session['m'] = x
      template = loader.get_template('alumniView.html')
      return HttpResponse(template.render({}, request))
    else:
      return HttpResponse("<script>alert('Invalid Credentials');window.history.back();</script>")
  