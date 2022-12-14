from django.urls import path
from . import views


urlpatterns = [   
    path('', views.index.as_view(), name='index'), 
    path('register', views.register.as_view(), name='register'),
    path('register/clinic', views.clinic_register.as_view(), name='clinic-register'),
    path('register/pharmacy', views.pharmacy_register.as_view(), name='pharmacy-register'),
	path('login', views.login.as_view(), name='login'),
    path('consultation', views.consultations.as_view(), name='Patient_Consultation'),
    path('consultation/cancel', views.CancelConsultations.as_view(), name='Patient_Consultation_Cancel'),
    path('pharmacy', views.pharmacy.as_view(), name='Patient_Presciptions'),
    path('bills', views.bills.as_view(), name='Patient_Bills'),
    path('profile', views.profile.as_view(), name='Patient_Profile'),
    path('contact-us', views.contact.as_view(), name='Contact-us'),
    path('logout', views.logout.as_view(), name='logout'),
]
