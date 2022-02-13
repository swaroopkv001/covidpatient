from django.urls import path

from  . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('patient/',views.Patient, name='Patient'),
    path('doctor/',views.Doctor, name='Doctor'),
    path('test/',views.test, name='test'),
    path('bed/',views.bed, name='bed'),
    path('hospital/',views.hospital, name='hospital'),
    path('report/',views.report, name='report'),
    path('login/',views.login, name='login'),
    #path('add',views.add, name='add')
]