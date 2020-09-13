from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in, name="sign_in"),
    path('sign-up/', views.sign_up, name="sign_up"),
    path('homepage/', views.homepage, name="homepage"),
    path('verification/', views.verification, name="verification"),
    path('menu/', views.menu, name="menu"),
    path('editprofile/', views.edit_profile, name="editprofile"),
    path('editfirstname/', views.edit_firstname, name='editfirstname'),
    path('editlastname/', views.edit_lastname, name='editlastname'),
    path('editpassword/', views.edit_password, name='editpassword'),
    path('viewprofile/', views.view_profile, name='viewprofile'),
    path('add_time/', views.add_time, name='add_time'),
    path('doctor_homepage/', views.doctor_page, name='doctor_page'),
    path('x/', views.x),
    path('viewss/', views.view_reserves, name="viewlist"),
    path('reserved_list/', views.reserved_list, name="reservedlist"),
    path('patient_list/', views.patient_list, name="patientlist"),
    path('visit_past/', views.delete_past, name="visitpast"),
    path('personal_record/', views.view_records, name="personalrecord"),
    path('cancel_visit/', views.cancel_visit, name="cancelvisit"),
]