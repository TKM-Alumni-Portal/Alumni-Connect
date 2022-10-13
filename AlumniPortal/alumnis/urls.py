from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('alumniReg/', views.alumniReg, name='alumniReg'),
    path('alumniReg/addUser/', views.addUser, name='addUser'),
    path('alumniReg/addUser/verifyAlumni/<int:id>', views.verifyAlumni, name='verifyAlumni'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('alumniSignIn', views.alumniSignIn, name='alumniSignIn'),
    path('alumniSignIn/authAlumni', views.authAlumni, name='authAlumni'),  # type: ignore
    path('alumniSignOut', views.alumniSignOut, name='alumniSignOut'),
    path('alumniSignIn/verifyAlumni2/<int:id>', views.verifyAlumni2, name='verifyAlumni2'),
]