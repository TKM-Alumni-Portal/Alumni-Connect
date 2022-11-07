from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    path('superAdmin', views.superAdmin, name='superAdmin'),
    path('test', views.test, name='test'),
    path('imgfile', views.imgfile, name='imgfile'),
    path('alumniProPic', views.alumniProPic, name='alumniProPic'),
    path('alumniReg/', views.alumniReg, name='alumniReg'),
    path('alumniView/', views.alumniView, name='alumniView'),  # type: ignore
    path('alumniReg/addUser/', views.addUser, name='addUser'),
    path('alumniReg/addUser/verifyAlumni/<int:id>', views.verifyAlumni, name='verifyAlumni'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('alumniSignIn', views.alumniSignIn, name='alumniSignIn'),
    path('alumniSignIn/authAlumni', views.authAlumni, name='authAlumni'),  # type: ignore
    path('alumniSignOut', views.alumniSignOut, name='alumniSignOut'),
    path('alumniSignIn/verifyAlumni2/<int:id>', views.verifyAlumni2, name='verifyAlumni2'),
    path('alumniProfile/', views.alumniProfile, name='alumniProfile'),
    path('FacultySignIn', views.FacultySignIn, name='FacultySignIn'),
    path('FacultySignIn/authFaculty', views.authFaculty, name='authFaculty'),  # type: ignore
    path('FacultySignOut', views.FacultySignOut, name='FacultySignOut'),
    path('FacultyView/', views.FacultyView, name='FacultyView'),
    path('AdminView/', views.AdminView, name='AdminView'),
    path('grantAccess/<int:id>', views.grantAccess, name="grantAccess"),
    path('revokeAccess/<int:id>', views.revokeAccess, name="revokeAccess"),
    path('completeProfile/', views.completeProfile, name='completeProfile'),
    path('completeProfile/addDetails/<str:email>', views.addDetails, name='addDetails'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)