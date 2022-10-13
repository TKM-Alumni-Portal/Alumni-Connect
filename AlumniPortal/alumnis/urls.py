from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alumniReg/', views.alumniReg, name='alumniReg'),
    path('alumniReg/addUser/', views.addUser, name='addUser'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('alumniSignIn', views.alumniSignIn, name='alumniSignIn'),
    path('alumniSignIn/authAlumni', views.authAlumni, name='authAlumni'),
    path('alumniSignOut', views.alumniSignOut, name='alumniSignOut'),
]