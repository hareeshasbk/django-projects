from django.db import models

# Create your models here.

class EmployeeInfo(models.Model):
 firstname = models.CharField(max_length=255)
 lastname = models.CharField(max_length=255)

class StudentInfo(models.Model):
 StudentName=models.CharField(max_length=255,default='None')
 StudentEmail=models.CharField(max_length=255,default='None')
 StudentAddress=models.CharField(max_length=255,default='None')

class EmployeeDetails(models.Model):
 club_name = models.CharField(max_length=255)
 joining_date = models.DateField()
 Employee=models.ForeignKey('EmployeeInfo',on_delete=models.CASCADE)


