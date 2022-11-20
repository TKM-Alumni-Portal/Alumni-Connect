from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin



urlpatterns = [
    path('', views.index, name='index'),
    path('upcomingEventsFaculty/',views.upcomingEventsFaculty, name="upcomingEventsFaculty"),
    path('upcomingEventsAlumni/',views.upcomingEventsAlumni, name="upcomingEventsAlumni"),
    path('changePassword',views.changePassword, name="changePassword"),
    path('changeFacultyPassword',views.changeFacultyPassword, name="changeFacultyPassword"),
    path('feedback', views.feedback, name='feedback'),
    path('superAdmin/', views.superAdmin, name='superAdmin'),
    path('sAdminSignIn', views.sAdminSignIn, name='sAdminSignIn'),
    path('sAdminSignIn/authSAdmin', views.authSAdmin, name='authSAdmin'),
    path('sAdminSignOut', views.sAdminSignOut, name='sAdminSignOut'),
    path('test', views.test, name='test'),
    path('alumniProfile/uploadProPic', views.uploadProPic, name = 'uploadProPic'),
    path('FacultyProfile/FacultyProPic', views.FacultyProPic, name = 'FacultyProPic'),
    path('alumniReg/', views.alumniReg, name='alumniReg'),
    path('alumniView/', views.alumniView, name='alumniView'),
    path('alumniApproval/', views.alumniApproval, name='alumniApproval'),  # type: ignore
    path('alumniReg/addUser/', views.addUser, name='addUser'),
    path('alumniReg/addUser/verifyAlumni/<str:email>', views.verifyAlumni, name='verifyAlumni'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('alumniSignIn', views.alumniSignIn, name='alumniSignIn'),
    path('alumniSignIn/authAlumni', views.authAlumni, name='authAlumni'),  # type: ignore
    path('alumniSignOut', views.alumniSignOut, name='alumniSignOut'),
    path('alumniProfile/', views.alumniProfile, name='alumniProfile'),
    path('adminAlumniList/', views.adminAlumniList, name='adminAlumniList'),
    path('FacultyProfile/', views.FacultyProfile, name='FacultyProfile'),
    path('FacultySignIn', views.FacultySignIn, name='FacultySignIn'),
    path('FacultySignIn/authFaculty', views.authFaculty, name='authFaculty'),  # type: ignore
    path('FacultySignOut', views.FacultySignOut, name='FacultySignOut'),
    path('FacultyView/', views.FacultyView, name='FacultyView'),
    path('AdminView/', views.AdminView, name='AdminView'),
    path('grantAccess/<str:email>', views.grantAccess, name="grantAccess"),
    path('revokeAccess/<str:email>', views.revokeAccess, name="revokeAccess"),
    path('completeProfile/', views.completeProfile, name='completeProfile'),
    path('completeProfile/addDetails/<str:email>', views.addDetails, name='addDetails'),
    path('alumniProfile/updateDetails/<str:email>', views.updateDetails, name='updateDetails'),
    path('alumniProfile/updatePreference/<str:email>', views.updatePreference, name='updatePreference'),
    path('alumniProfile/deleteProPic/<str:email>', views.deleteProPic, name='deleteProPic'),
    path('alumniList/', views.alumniList, name='alumniList'),
    path('FacultyProfile/deleteFacultyProPic/<str:email>', views.deleteFacultyProPic, name='deleteFacultyProPic'),
    path('addEvent/', views.addEvent, name='addEvent'),
    path('addEventDetails/', views.addEventDetails, name='addEventDetails'),
    path('completedEventsFaculty/', views.completedEventsFaculty, name='completedEventsFaculty'),
    path('completedEventsAlumni/', views.completedEventsAlumni, name='completedEventsAlumni'),
    path('approveUser/<str:email>', views.approveUser, name="approveUser"),
    path('viewAlumni/<str:email>', views.viewAlumni, name="viewAlumni"),
    path('facultyGallery/', views.facultyGallery, name="facultyGallery"),
    path('allEventsFaculty/', views.allEventsFaculty, name="allEventsFaculty"),
    path('viewFeedbacks/', views.viewFeedbacks, name="viewFeedbacks"),
    path('positivemail/<str:email>', views.positivemail, name="positivemail"),
    path('negativemail/<str:email>', views.negativemail, name="negativemail"),
    path('addFaculty/', views.addFaculty, name='addFaculty'),
    path('addFacultyDetails/', views.addFacultyDetails, name='addFacultyDetails'),
    path('approveEvent/<str:date>', views.approveEvent, name='approveEvent'),
    path('deleteEvent/<str:date>', views.deleteEvent, name='deleteEvent'),
    path('viewAlumniPro/<str:email>', views.viewAlumniPro, name="viewAlumniPro"),
    path('alumniGallery/', views.alumniGallery, name="alumniGallery"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)