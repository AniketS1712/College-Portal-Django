from django.db import models

class Students(models.Model):
    Enrollment_no = models.IntegerField()
    S_Name = models.CharField(max_length=20)
    S_Age = models.IntegerField()
    Course = models.CharField(max_length=5)
    College = models.CharField(max_length=10)

class faculty(models.Model):
    F_Name = models.CharField(max_length=20)
    F_Designation = models.CharField(max_length=20)
    Subject = models.CharField(max_length=20)
    Department = models.CharField(max_length=20)
    Educational_Qualification = models.CharField(max_length=50)
    Email = models.EmailField()
    Specialization = models.CharField(max_length=50)
    Field_of_Interest = models.CharField(max_length=100)
    Teaching_Experience = models.IntegerField()