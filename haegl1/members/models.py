from django.db import models

# Create your models here.

class EmployeeInfo(models.Model):
 firstname = models.CharField(max_length=255)
 lastname = models.CharField(max_length=255)

class StudentInfo(models.Model):
 StudentName=models.CharField(max_length=255,default='None')
 StudentEmail=models.CharField(max_length=255,default='None')
 StudentAddress=models.CharField(max_length=255,default='None')



