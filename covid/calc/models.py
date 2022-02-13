from pickle import FALSE
from pickletools import TAKEN_FROM_ARGUMENT1

from django.db import models
from django.forms import IntegerField

# Create your models here.
class Hospital(models.Model):
    Hospital_name=models.CharField(max_length=100)
    Hospital_address= models.CharField(max_length=100)

class Doctor(models.Model):
    Dr_name=models.CharField(max_length=70,null=True,blank=True)
    Specialization=models.CharField(max_length=50,null=True,blank=True)
    hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE,default=True,null=True)

class Patients(models.Model):
   pno=models.IntegerField(null=True,blank=True)
   fname = models.CharField(max_length=20,null=True,blank=True)
   lname = models.CharField(max_length=20,null=True,blank=True)
   #age = models.IntegerField(null=True,blank=True)
   address = models.CharField(max_length=150,null=True,blank=True)
   Dr=models.ForeignKey(Doctor,on_delete=models.CASCADE,default=True,null=True)
   hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE,default=True,null=True)

   
class Test(models.Model):
    RTPCR=models.CharField(max_length=20)
    Rap_antigen=models.CharField(max_length=20)
    patient=models.ForeignKey(Patients,on_delete=models.CASCADE,default=True,null=True)

class Bed_avail(models.Model):
    ICU=models.IntegerField()
    Special=models.IntegerField()
    General=models.IntegerField()
    hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE,default=True,null=True)

class Report(models.Model):
    Condition=models.CharField(max_length=50)
    Discharge_date=models.DateField()
    result=models.ForeignKey(Test,on_delete=models.CASCADE,default=True,null=True)
        
class Login(models.Model):
      name=models.CharField(max_length=30)
      email=models.CharField(max_length=30)
      password1=models.CharField(max_length=30)