from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse
from requests import session
from .models import Alumnis
import random

from django.conf import settings
from django.core.mail import send_mail

def index(request):
  ouralumnis = Alumnis.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'ouralumnis': ouralumnis,
  }
  return HttpResponse(template.render(context, request))

def test(request):
  ouralumnis = Alumnis.objects.all().values()
  context = {
    'ouralumnis': ouralumnis,
  }
  template = loader.get_template('test.html')
  return HttpResponse(template.render(context, request))

def alumniReg(request):
  template = loader.get_template('alumniReg.html')
  return HttpResponse(template.render({}, request))

def addUser(request):
  u = request.POST['fname']
  v = request.POST['lname']
  w = request.POST['mobile']
  x = request.POST['mail']
  y = request.POST['psw']
  y1 = request.POST['cpsw']
  z = random.randint(100000,999999)
  mydata = Alumnis.objects.all()
  flag=0
  for i in mydata:
    if i.email==x:
      flag=1
      break
  if flag==1:
    return HttpResponse("<script>alert('Email Id Already Exist!');window.history.back();</script>")
  else:
    if y1!=y:
      return HttpResponse("<script>alert('Password Does not Match!');window.history.back();</script>")
    else:  
      a = Alumnis(fname=u,lname=v, email=x, mobile=w, password=y, otp=z)
      a.save()
      subject = 'Welcome to the Alumni-Connect'
      message = f'Hi '+u+' '+v+', Thank you for Joining in Alumni-Connect.'
      email_from = settings.EMAIL_HOST_USER
      recipient_list = [x, ]
      send_mail( subject, message, email_from, recipient_list )
      subject = 'Verify Your Account'
      message = f'Hi '+u+' '+v+', '+str(z)+f' is Your One Time Password for account verification.'
      email_from = settings.EMAIL_HOST_USER
      recipient_list = [x, ]
      send_mail( subject, message, email_from, recipient_list )
      template = loader.get_template('verifyAlumni.html')
      context = {
        'al':a
      }
      return HttpResponse(template.render(context, request))

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
  fname = request.POST['fname']
  lname = request.POST['lname']
  mobile = request.POST['mobile']
  mail = request.POST['mail']
  psw = request.POST['psw']
  verified = request.POST['verified']
  al = Alumnis.objects.get(id=id)
  al.fname = fname
  al.lname = lname
  al.email = mail
  al.mobile = mobile
  al.password = psw
  al.verified = verified
  al.save()
  return HttpResponseRedirect(reverse('index'))

def superAdmin(request):
  template = loader.get_template('superAdminView.html')
  return HttpResponse(template.render({}, request))

def alumniSignIn(request):
  template = loader.get_template('alumniSignIn.html')
  return HttpResponse(template.render({}, request))

def alumniSignOut(request):
  if 'email' in request.session:
    request.session.flush()
  return redirect(alumniSignIn)

def alumniView(request):
  if 'email' in request.session:
    a=request.session.get('email')
    user = Alumnis.objects.filter(email=a).values()
    template = loader.get_template('alumniView.html')
    context = {
    'myalumnis': user,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('alumniSignIn')

def authAlumni(request):
  x = request.POST['mail']
  y = request.POST['psw']
  mydata = Alumnis.objects.all()
  flag=0
  for i in mydata:
    if i.email==x and i.password==y and i.verified==1:
      flag=1
      break
    elif i.email==x and i.verified==1 or i.password==y and i.verified==1:
      flag=2
    elif i.email==x and i.password==y and i.verified==0:
      flag=3
  if flag==1:
    request.session['email'] = x
    return redirect('alumniView')
  elif flag==2:
    return HttpResponse("<script>alert('Invalid Credentials!');window.history.back();</script>")
  elif flag==3:
    mydata = Alumnis.objects.all()
    for i in mydata:
      if i.email==x:
        template = loader.get_template('verifyAlumni2.html')
        context = {
          'al': i
        }
        request.session['email'] = x
        return HttpResponse(template.render(context, request))

  else:
    return HttpResponse("<script>alert('No account belongs to the details entered!');window.history.back();</script>")


def verifyAlumni(request,id):
  o = request.POST['otp']
  al = Alumnis.objects.get(id=id)
  if str(al.otp)==o:
    al.verified=1
    al.save()
    return HttpResponseRedirect('../../../alumniSignIn')
  else:
    return HttpResponse("<script>alert('Enter Valid OTP');window.history.back();</script>")

def verifyAlumni2(request,id):
  o = request.POST['otp']
  al = Alumnis.objects.get(id=id)
  if str(al.otp)==o:
    al.verified=1
    al.save()
    return HttpResponseRedirect('../../alumniSignIn')
  else:
    return HttpResponse("<script>alert('Enter Valid OTP');window.history.back();</script>")
def alumniProfile(request):
  if 'email' in request.session:
    a=request.session.get('email')
    user = Alumnis.objects.filter(email=a).values()
    template = loader.get_template('alumniProfile.html')
    context = {
    'myalumnis': user,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('alumniSignIn')