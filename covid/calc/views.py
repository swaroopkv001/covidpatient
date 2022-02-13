#from http.client import HTTPResponse
from wsgiref.util import request_uri
from django.shortcuts import render
from django.http import HttpResponse

#from calc.models import Patients
from calc.models import *

# Create your views here.
def home(request):
   
   return render(request, 'home.html')
 
def Patient(request):
   if request.method=="POST":
       patient_id=request.POST.get("txtCustomerID")
       fname=request.POST.get("txtCustomerName")
       lname=request.POST.get("txtContactName")
       address=request.POST.get("txtAddress")
       Dr=request.POST.get("txtPostalCode")
       hospital=request.POST.get("txtHospital_id")
      
       patient_info=Patients(pno=patient_id,fname=fname,lname=lname,address=address,Dr=Dr,hospital=hospital)
       print("data saved")
       patient_info.save()
      
       return render(request, 'Patient.html')
   else:
       return render(request, 'Patient.html')

def Doctor(request):
    if request.method=="POST":
        Dr=request.POST.get("txtCustomerName")
        Specialization=request.POST.get("txtContactName")
        hospital=request.POST.get("txtAddress")

        doctor_info=Doctor(Dr_name=Dr,Specialization=Specialization,hospital=hospital)
        doctor_info.save()
        return render(request, 'doctor.html')
    else:
        return render(request, 'doctor.html')

def bed(request):
    if request.method=="POST":
        ICU=request.get.POST("txtCustomerName")
        Special=request.get.POST("txtContactName")
        General=request.get.POST("txtAddress")
        hospital=request.get.POST("txtPostalCode")
        
        bed_info=Bed_avail(ICU=ICU,Special=Special,General=General,hospital=hospital)
        bed_info.save()
        return render(request, 'bed.html')

    else:
         return render(request, 'bed.html')

def test(request):
    if request.method=="POST":
        RTPCR=request.get.POST("txtCustomerName")
        Rap_antigen=request.get.POST("txtContactName")
        patient=request.get.POST("txtAddress")

        test_info=Test(RTPCR=RTPCR,Rap_antigen=Rap_antigen,patient=patient)
        test_info.save()
        return render(request, 'test.html')

    else:
        return render(request, 'test.html')
def hospital(request):
     if request.method=="POST":
        hospital=request.get.POST("txtCustomerName")
        hospital_add=request.get.POST("txtContactName")

        hospital_info=Hospital(Hospital_name=hospital,Hospital_address=hospital_add)
        hospital_info.save()
        return render(request, 'hospital.html')
        
     else:
        return render(request, 'hospital.html')

def report(request):
        return render(request, 'report.html')

def login(request):
    if request.method=="POST":
        name=request.get.POST("username")
        email=request.get.POST("mail")
        password=request.get.POST("pass")
        login_info=Login(name=name,email=email,password1=password)
        login_info.save()
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')

