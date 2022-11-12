from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin



urlpatterns = [
    path('', views.index, name='index'),
    path('superAdmin', views.superAdmin, name='superAdmin'),
    path('test', views.test, name='test'),
    path('alumniProfile/uploadProPic', views.uploadProPic, name = 'uploadProPic'),
    path('FacultyProfile/FacultyProPic', views.FacultyProPic, name = 'FacultyProPic'),
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
    path('alumniProfile/', views.alumniProfile, name='alumniProfile'),
    path('FacultyProfile/', views.FacultyProfile, name='FacultyProfile'),
    path('FacultySignIn', views.FacultySignIn, name='FacultySignIn'),
    path('FacultySignIn/authFaculty', views.authFaculty, name='authFaculty'),  # type: ignore
    path('FacultySignOut', views.FacultySignOut, name='FacultySignOut'),
    path('FacultyView/', views.FacultyView, name='FacultyView'),
    path('AdminView/', views.AdminView, name='AdminView'),
    path('grantAccess/<int:id>', views.grantAccess, name="grantAccess"),
    path('revokeAccess/<int:id>', views.revokeAccess, name="revokeAccess"),
    path('completeProfile/', views.completeProfile, name='completeProfile'),
    path('completeProfile/addDetails/<str:email>', views.addDetails, name='addDetails'),
    path('alumniProfile/updateDetails/<str:email>', views.updateDetails, name='updateDetails'),
    path('alumniProfile/updatePreference/<str:email>', views.updatePreference, name='updatePreference'),
    path('alumniProfile/deleteProPic/<str:email>', views.deleteProPic, name='deleteProPic'),
    path('alumniList/', views.alumniList, name='alumniList'),
    path('FacultyProfile/deleteFacultyProPic/<str:email>', views.deleteFacultyProPic, name='deleteFacultyProPic'),
    path('addEvent', views.addEvent, name='addEvent'),
    path('addEventDetails', views.addEventDetails, name='addEventDetails'),
    path('upcomingFacultyEvents', views.upcomingFacultyEvents, name='upcomingFacultyEvents'),
    path('completedFacultyEvents', views.completedFacultyEvents, name='completedFacultyEvents'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)