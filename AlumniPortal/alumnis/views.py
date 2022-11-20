import hashlib
import random
from datetime import date
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from requests import session

from .models import *


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
  b = request.POST['branch']
  ad = request.POST['yoa']
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
      a = Alumnis(fname=u,lname=v, email=x, mobile=w, password=y, otp=z, branch=b, yoa=ad)
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
  if 'email' in request.session:
    mydata = Faculty.objects.all()
    template = loader.get_template('superAdminView.html')
    context = {
      'faculty': mydata,
    }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def sAdminSignOut(request):
  if 'email' in request.session:
    request.session.flush()
  return redirect(sAdminSignIn)

def sAdminSignIn(request):
  template = loader.get_template('sAdminSignIn.html')
  return HttpResponse(template.render({}, request))

def authSAdmin(request):
  x = request.POST['penNo']
  y = request.POST['psw']
  if x == "tkmce.alumniportal@gmail.com" and y == "Super@123":
    request.session['email'] = x
    return redirect('superAdmin')
  else:
    return HttpResponse("<script>alert('Invalid Credentials!');window.history.back();</script>") 

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
    pic = AlumniProPic.objects.filter(email=a).values()
    user = Alumnis.objects.filter(email=a).values()
    alumniDetails = AlumniProfile.objects.filter(email=a).values()
    template = loader.get_template('alumniView.html')
    context = {
    'myalumnis': user,'details':alumniDetails,'pic' : pic,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

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
    mydata = Alumnis.objects.all()
    for i in mydata:
      if i.email==x:
        if i.profile==0 or i.profile==2:
          return redirect('completeProfile')
        elif i.profile==1:
          return redirect('alumniView')
  elif flag==2:
    return HttpResponse("<script>alert('Invalid Credentials!');window.history.back();</script>")
  elif flag==3:
    mydata = Alumnis.objects.all()
    for i in mydata:
      if i.email==x:
        template = loader.get_template('verifyAlumni.html')
        context = {
          'al': i
        }
        request.session['email'] = x
        return HttpResponse(template.render(context, request))

  else:
    return HttpResponse("<script>alert('No account belongs to the details entered!');window.history.back();</script>")


def verifyAlumni(request,email):
  o = request.POST['otp']
  al = Alumnis.objects.get(email=email)
  if str(al.otp)==o:
    al.verified=1
    al.save()
    return HttpResponseRedirect('../../../alumniSignIn')
  else:
    return HttpResponse("<script>alert('Enter Valid OTP');window.history.back();</script>")

def alumniProfile(request):
  if 'email' in request.session:
    a=request.session.get('email')
    pic = AlumniProPic.objects.filter(email=a).values()
    user = Alumnis.objects.filter(email=a).values()
    alumniDetails = AlumniProfile.objects.filter(email=a).values()
    template = loader.get_template('alumniProfile.html')
    context = {
    'myalumnis': user,'details':alumniDetails,'pic' : pic,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def FacultySignIn(request):
  template = loader.get_template('FacultySignIn.html')
  return HttpResponse(template.render({}, request))

def FacultySignOut(request):
  if 'email' in request.session:
    request.session.flush()
  return redirect(FacultySignIn)

def authFaculty(request):
  x = request.POST['penNo']
  y = request.POST['psw']
  mydata = Faculty.objects.all()
  flag=0
  u=""
  v=""
  for i in mydata:
    if i.penNumber==x and i.password==y and i.access==0:
      flag=1
      u=i.email
      break
    elif i.penNumber==x and i.password==y and i.access==1:
      flag=2
      v=i.email
      break
  if flag==1:
    request.session['email'] = u
    return redirect('FacultyView')
  elif flag==2:
    request.session['email'] = v
    return redirect('AdminView')
  else:
    return HttpResponse("<script>alert('Invalid Credentials!');window.history.back();</script>")

def FacultyView(request):
  if 'email' in request.session:
    f=request.session.get('email')
    user = Faculty.objects.filter(email=f).values()
    template = loader.get_template('FacultyView.html')
    context = {
    'myFaculty': user,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def AdminView(request):
  if 'email' in request.session:
    f=request.session.get('email')
    user = Faculty.objects.filter(email=f).values()
    alumniList =Alumnis.objects.filter(profile=1)
    alumniD=[]
    for i in alumniList:
      cp=AlumniProfile.objects.filter(email=i.email).count()
      ci=AlumniProPic.objects.filter(email=i.email).count()
      if int(cp)>0 and int(ci)>0:
        x=AlumniProfile.objects.get(email=i.email)
        y=AlumniProPic.objects.get(email=i.email)
        alumniD.append([i.email,i.fname,i.lname,x.linkedID,y.proPic])
      elif int(cp)>0 and int(ci)==0:
        x=AlumniProfile.objects.get(email=i.email)
        alumniD.append([i.email,i.fname,i.lname,x.linkedID,0])
    template = loader.get_template('AdminView.html')
    context = {
    'myFaculty': user,'alumniList': alumniD,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def grantAccess(request,email):
  al = Faculty.objects.get(email=email)
  al.access=1
  al.save()
  return HttpResponseRedirect(reverse('superAdmin'))

def revokeAccess(request,email):
  al = Faculty.objects.get(email=email)
  al.access=0
  al.save()
  return HttpResponseRedirect(reverse('superAdmin'))

def completeProfile(request):
  if 'email' in request.session:
    a=request.session.get('email')
    user = Alumnis.objects.filter(email=a).values()
    template = loader.get_template('completeProfile.html')
    context = {'myalumnis': user,}
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def addDetails(request, email):
  industry = request.POST['industry']
  position = request.POST['position']
  location = request.POST['location']
  specialization = request.POST['specialization']
  linkedId = request.POST['linkedId']
  gf = request.POST['gf']
  cs = request.POST['cs']
  fi = request.POST['fi']
  r = request.POST['r']
  fdp = request.POST['fdp']
  mdp = request.POST['mdp']
  iv = request.POST['iv']
  bs = request.POST['bs']
  c = request.POST['c']
  sip = request.POST['sip']
  p = request.POST['p']
  ic = request.POST['ic']
  lps = request.POST['lps']
  csr = request.POST['csr']
  ssp = request.POST['ssp']
  se = request.POST['se']
  add = AlumniProfile(email=email,industry=industry, position=position, location=location, specialization=specialization, linkedID=linkedId, gf=gf, cs=cs, fi=fi, research=r,fdp=fdp, mdp=mdp, iv=iv, buddySys=bs, consulting=c, sip=sip, placements=p, ic=ic, lps=lps, csr=csr, ssp=ssp, se=se)
  add.save()
  user = Alumnis.objects.get(email=email)
  user.profile = 2
  user.save()
  return HttpResponseRedirect(reverse('completeProfile'))

def updatePreference(request, email):
  industry = request.POST['industry']
  position = request.POST['position']
  location = request.POST['location']
  specialization = request.POST['specialization']
  linkedId = request.POST['linkedId']
  gf = request.POST['gf']
  cs = request.POST['cs']
  fi = request.POST['fi']
  r = request.POST['r']
  fdp = request.POST['fdp']
  mdp = request.POST['mdp']
  iv = request.POST['iv']
  bs = request.POST['bs']
  c = request.POST['c']
  sip = request.POST['sip']
  p = request.POST['p']
  ic = request.POST['ic']
  lps = request.POST['lps']
  csr = request.POST['csr']
  ssp = request.POST['ssp']
  se = request.POST['se']
  prefer = Alumnis.objects.get(email=email)
  prefer = AlumniProfile(industry=industry, position=position, location=location, specialization=specialization, linkedID=linkedId, gf=gf, cs=cs, fi=fi, research=r,fdp=fdp, mdp=mdp, iv=iv, buddySys=bs, consulting=c, sip=sip, placements=p, ic=ic, lps=lps, csr=csr, ssp=ssp, se=se)
  prefer.save()

  return HttpResponseRedirect(reverse('alumniView'))

def updateDetails(request,email):
  fname = request.POST['fname']
  lname = request.POST['lname']
  mobile = request.POST['mobile']
  industry = request.POST['industry']
  position = request.POST['position']
  location = request.POST['location']
  linkedID = request.POST['linkedID']
  al = Alumnis.objects.get(email=email)
  aD = AlumniProfile.objects.get(email=email)
  al.fname = fname
  al.lname = lname
  al.mobile = mobile
  aD.industry = industry
  aD.position = position
  aD.location = location
  aD.linkedID = linkedID
  al.save()
  aD.save()
  return HttpResponseRedirect(reverse('alumniProfile'))

def uploadProPic(request):
    if request.method == 'POST' and request.FILES['proPic']:
        proPic = request.FILES['proPic']
        img=AlumniProPic(email=request.session.get('email'),proPic=proPic)
        img.save()
        return redirect('alumniProfile')
    return HttpResponse("Failed to upload")

def deleteProPic(request, email):
  a = AlumniProPic.objects.get(email=email)
  a.delete()
  return HttpResponseRedirect(reverse('alumniProfile'))

def alumniList(request):
  if 'email' in request.session:
    a=request.session.get('email')
    pic = AlumniProPic.objects.filter(email=a).values()
    user = Alumnis.objects.filter(email=a).values()
    alumniDetails = AlumniProfile.objects.filter(email=a).values()
    alumniList =Alumnis.objects.filter(~Q(email=a),profile=1)
    alumniD=[]
    for i in alumniList:
      cp=AlumniProfile.objects.filter(email=i.email).count()
      ci=AlumniProPic.objects.filter(email=i.email).count()
      if int(cp)>0 and int(ci)>0:
        x=AlumniProfile.objects.get(email=i.email)
        y=AlumniProPic.objects.get(email=i.email)
        alumniD.append([i.email,i.fname,i.lname,x.linkedID,y.proPic])
      elif int(cp)>0 and int(ci)==0:
        x=AlumniProfile.objects.get(email=i.email)
        alumniD.append([i.email,i.fname,i.lname,x.linkedID,0])
    template = loader.get_template('alumniList.html')
    context = {
    'myalumnis': user,'details':alumniDetails,'pic' : pic, 'alumniList': alumniD,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def addEvent(request):
  if 'email' in request.session:
    a=request.session.get('email')
    user = Faculty.objects.filter(email=a).values()
    template = loader.get_template('addEvent.html')
    context = {
    'myFaculty': user,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def FacultyProfile(request):
  if 'email' in request.session:
    a=request.session.get('email')
    user = Faculty.objects.filter(email=a).values()
    template = loader.get_template('FacultyProfile.html')
    context = {
    'myFaculty': user,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')  

def FacultyProPic(request):
  if request.method == 'POST' and request.FILES['proPic']:
    proPic = request.FILES['proPic']
    email=request.session.get('email')
    user=Faculty.objects.get(email=email)
    user.proPic=proPic
    user.save()
    return redirect('FacultyProfile')
  return HttpResponse("Failed to upload")
def deleteFacultyProPic(request, email):
  a = Faculty.objects.get(email=email)
  a.proPic=""  # type: ignore
  a.save()
  return HttpResponseRedirect(reverse('FacultyProfile'))
def addEventDetails(request):
  a=request.session.get('email')
  d = Faculty.objects.get(email=a)
  ename = request.POST['ename']
  date = request.POST['date']
  time = request.POST['time']
  description = request.POST['description']
  mode = request.POST['mode']
  pic = request.FILES['pic']
  if d.access==0:
    ae=Events(name=ename,date=date,time=time,description=description,mode=mode,pic=pic)
    ae.save()
    return HttpResponseRedirect(reverse('FacultyView'))
  else:
    ae=Events(name=ename,date=date,time=time,description=description,mode=mode,pic=pic,status=1)
    ae.save()
    return HttpResponseRedirect(reverse('allEventsFaculty'))
def upcomingFacultyEvents(request):
  if 'email' in request.session:
    a=request.session.get('email')
    user = Faculty.objects.filter(email=a).values()
    template = loader.get_template('FacultyUpComingEvents.html')
    context = {
    'myFaculty': user,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')
def completedFacultyEvents(request):
  if 'email' in request.session:
    a=request.session.get('email')
    user = Faculty.objects.filter(email=a).values()
    template = loader.get_template('FacultyCompletedEvents.html')
    context = {
    'myFaculty': user,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def feedback(request):
  name = request.POST['name']
  email = request.POST['email']
  sub = request.POST['subject']
  message = request.POST['message']
  f = Feedbacks(name=name, email=email, subject=sub, message=message)
  f.save()
  return HttpResponse("<script>alert('Your message has been sent. Thank you!');window.location.href='../alumnis';</script>")

def changePassword(request):
  cpass = request.POST['currentPassword']
  npass = request.POST['newpassword']
  rpass = request.POST['renewpassword']
  a=request.session.get('email')
  user = Alumnis.objects.get(email=a)
  if user.password == cpass:
    if npass!=rpass:
      return HttpResponse("<script>alert('New password and reentered password doesnot match!');window.history.back();</script>")
    else:
      user.password=npass
      user.save()
      return HttpResponse("<script>alert('Password Changed Successfully!');window.location.href='../alumniProfile';</script>")
  else:
      return HttpResponse("<script>alert('Incorrect Current Password!');window.history.back();</script>")

def adminAlumniList(request):
  if 'email' in request.session:
    a=request.session.get('email')
    user = Faculty.objects.filter(email=a).values()
    alumniList =Alumnis.objects.filter(profile=1)
    alumniD=[]
    for i in alumniList:
      cp=AlumniProfile.objects.filter(email=i.email).count()
      ci=AlumniProPic.objects.filter(email=i.email).count()
      if int(cp)>0 and int(ci)>0:
        x=AlumniProfile.objects.get(email=i.email)
        y=AlumniProPic.objects.get(email=i.email)
        alumniD.append([i.email,i.fname,i.lname,x.linkedID,y.proPic])
      elif int(cp)>0 and int(ci)==0:
        x=AlumniProfile.objects.get(email=i.email)
        alumniD.append([i.email,i.fname,i.lname,x.linkedID,0])
    template = loader.get_template('AdminAlumniList.html')
    context = {
    'myFaculty': user,'alumniList': alumniD,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def alumniApproval(request):
  if 'email' in request.session:
    a=request.session.get('email')
    user = Faculty.objects.filter(email=a).values()
    ouralumnis = Alumnis.objects.filter(profile=2)
    alumniD=[]
    for i in ouralumnis:
      
      cp=AlumniProfile.objects.filter(email=i.email).count()
      ci=AlumniProPic.objects.filter(email=i.email).count()
      if int(cp)>0 and int(ci)>0:
        y=AlumniProPic.objects.get(email=i.email)
        alumniD.append([i.fname,i.lname,i.email,i.profile,y.proPic])
      elif int(cp)>0 and int(ci)==0:
        alumniD.append([i.fname,i.lname,i.email,i.profile,0])

    template = loader.get_template('ApproveAlumni.html')
    context = {
    'myFaculty': user,'ouralumnis': alumniD,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def approveUser(request,email):
  al = Alumnis.objects.get(email=email)
  al.profile=1
  al.save()
  return HttpResponseRedirect('../alumniApproval')

def viewAlumni(request,email):
  if 'email' in request.session:
    a=request.session.get('email')
    user = Faculty.objects.filter(email=a).values()
    pic = AlumniProPic.objects.filter(email=email).values()
    al = Alumnis.objects.filter(email=email).values()
    alumniDetails = AlumniProfile.objects.filter(email=email).values()
    template = loader.get_template('AdminAlumniPro.html')
    context = {
    'myFaculty': user,'pic' : pic,'details':alumniDetails,'alumni':al,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def changeFacultyPassword(request):
  cpass = request.POST['currentPassword']
  npass = request.POST['newpassword']
  rpass = request.POST['renewpassword']
  a=request.session.get('email')
  user = Faculty.objects.get(email=a)
  if user.password == cpass:
    if npass!=rpass:
      return HttpResponse("<script>alert('New password and reentered password doesnot match!');window.history.back();</script>")
    else:
      user.password=npass
      user.save()
      return HttpResponse("<script>alert('Password Changed Successfully!');window.location.href='/FacultyProfile';</script>")
  else:
      return HttpResponse("<script>alert('Incorrect Current Password!');window.history.back();</script>")

def upcomingEventsFaculty(request):
  if 'email' in request.session:
    a=request.session.get('email')
    user = Faculty.objects.filter(email=a).values()
    events = Events.objects.all()
    event=[]
    for i in events:
      if i.status==1:
        if i.date > date.today():
          if i.pic:
            event.append([i.name,i.date,i.time,i.description,i.mode,i.pic])
          else:
            event.append([i.name,i.date,i.time,i.description,i.mode,0])
    template = loader.get_template('FacultyUpComingEvents.html')
    context = {
    'myFaculty': user,'events': event,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')
def completedEventsFaculty(request):
  if 'email' in request.session:
    a=request.session.get('email')
    user = Faculty.objects.filter(email=a).values()
    events = Events.objects.all()
    event=[]
    for i in events:
      if i.status==1:
        if i.date < date.today():
          if len(i.description)>100:
            i.description=i.description[0:100]+"..."
          if i.pic:
            event.append([i.name,i.date,i.time,i.description,i.mode,i.pic])
          else:
            event.append([i.name,i.date,i.time,i.description,i.mode,0])
    template = loader.get_template('FacultyCompletedEvents.html')
    context = {
    'myFaculty': user,'events': event,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def upcomingEventsAlumni(request):
  if 'email' in request.session:
    a=request.session.get('email')
    pic = AlumniProPic.objects.filter(email=a).values()
    user = Alumnis.objects.filter(email=a).values()
    alumniDetails = AlumniProfile.objects.filter(email=a).values()
    events = Events.objects.all()
    event=[]
    for i in events:
      if i.status==1:
        if i.date > date.today():
          if i.pic:
            event.append([i.name,i.date,i.time,i.description,i.mode,i.pic])
          else:
            event.append([i.name,i.date,i.time,i.description,i.mode,0])
    template = loader.get_template('alumniUpComingEvents.html')
    context = {
    'myalumnis': user,'details':alumniDetails,'pic' : pic,'events': event,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def completedEventsAlumni(request):
  if 'email' in request.session:
    a=request.session.get('email')
    pic = AlumniProPic.objects.filter(email=a).values()
    user = Alumnis.objects.filter(email=a).values()
    alumniDetails = AlumniProfile.objects.filter(email=a).values()
    events = Events.objects.all()
    event=[]
    for i in events:
      if i.status==1:
        if i.date < date.today():
          if len(i.description)>100:
            i.description=i.description[0:100]+"..."
          if i.pic:
            event.append([i.name,i.date,i.time,i.description,i.mode,i.pic])
          else:
            event.append([i.name,i.date,i.time,i.description,i.mode,0])
    template = loader.get_template('alumniCompletedEvents.html')
    context = {
    'myalumnis': user,'details':alumniDetails,'pic' : pic,'events': event,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def allEventsFaculty(request):
  if 'email' in request.session:
    a=request.session.get('email')
    user = Faculty.objects.filter(email=a).values()
    events = Events.objects.all().order_by('-date').values()
    template = loader.get_template('allEventsFaculty.html')
    context = {
    'myFaculty': user, 'events':events,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def facultyGallery(request):
  if 'email' in request.session:
    a=request.session.get('email')
    user = Faculty.objects.filter(email=a).values()
    events = Events.objects.filter(status=1).order_by('-date')
    template = loader.get_template('FacultyGallery.html')
    context = {
    'myFaculty': user,'events':events,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def viewFeedbacks(request):
  if 'email' in request.session:
    a=request.session.get('email')
    user = Faculty.objects.filter(email=a).values()
    feedback =Feedbacks.objects.filter(status=0).order_by('-date')
    template = loader.get_template('viewFeedbacks.html')
    context = {
    'myFaculty': user,'feedback':feedback,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def positivemail(request,email):
  subject = 'Thank you for your Valuable Feedback.'
  u = Feedbacks.objects.get(email=email)
  message = f'Hi '+u.name+', Thank you for contacting Alumni-Connect. We value valuable feedbacks from users. You can contact us if you find any difficulties in our site. We are always here for you.'
  email_from = settings.EMAIL_HOST_USER
  recipient_list = [email, ]
  send_mail( subject, message, email_from, recipient_list )
  u.status=1
  u.save()
  return HttpResponseRedirect('../viewFeedbacks')

def negativemail(request,email):
  subject = 'Sorry for the inconvenience.'
  u = Feedbacks.objects.get(email=email)
  message = f'Hi '+u.name+', Sorry for the inconvenience, We will resolve the issue as soon as possible and Thank you for contacting us.'
  email_from = settings.EMAIL_HOST_USER
  recipient_list = [email, ]
  send_mail( subject, message, email_from, recipient_list )
  u = Feedbacks.objects.get(email=email)
  u.status=1
  u.save()
  return HttpResponseRedirect('../viewFeedbacks')


def addFacultyDetails(request):
  if 'email' in request.session:
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    mobile = request.POST['mobile']
    penNumber = request.POST['penNumber']
    f = Faculty(fname=fname, lname=lname, email=email, mobile=mobile, penNumber=penNumber,password=penNumber)
    f.save()
    return HttpResponseRedirect('../superAdmin')
  else:
    return redirect('index')

def addFaculty(request):
  if 'email' in request.session:
    template = loader.get_template('addFaculty.html')
    return HttpResponse(template.render({}, request))
  else:
    return redirect('index')

def approveEvent(request,date):
  event = Events.objects.get(date=date)
  event.status=1
  event.save()
  return HttpResponseRedirect('../allEventsFaculty')

def deleteEvent(request, date):
  event = Events.objects.get(date=date)
  event.delete()
  return HttpResponseRedirect('../allEventsFaculty')
def viewAlumniPro(request,email):
  if 'email' in request.session:
    a=request.session.get('email')
    pic = AlumniProPic.objects.filter(email=a).values()
    user = Alumnis.objects.filter(email=a).values()
    alumniDetails = AlumniProfile.objects.filter(email=a).values()
    alpic = AlumniProPic.objects.filter(email=email).values()
    al = Alumnis.objects.filter(email=email).values()
    alumniProDetails = AlumniProfile.objects.filter(email=email).values()
    template = loader.get_template('viewAlumniPro.html')
    context = {
    'myalumnis': user,'details':alumniDetails,'pic' : pic, 'alpic': alpic,'al':al,'aldetails':alumniProDetails,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')

def alumniGallery(request):
  if 'email' in request.session:
    a=request.session.get('email')
    pic = AlumniProPic.objects.filter(email=a).values()
    user = Alumnis.objects.filter(email=a).values()
    alumniDetails = AlumniProfile.objects.filter(email=a).values()
    events = Events.objects.filter(status=1).order_by('-date')
    template = loader.get_template('alumniGallery.html')
    context = {
    'myalumnis': user,'details':alumniDetails,'pic' : pic, 'events': events,
  }
    return HttpResponse(template.render(context, request))
  else:
    return redirect('index')