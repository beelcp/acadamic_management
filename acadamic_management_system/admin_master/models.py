from django.db import models

# Create your models here.

class AmsClass(models.Model):
    class_name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)

class AmsDepartment(models.Model):
    department_name = models.CharField(max_length=100)
    department_code = models.CharField(max_length=10)
    status = models.BooleanField(default=True)

class AmsDesignation(models.Model):
    designation_name = models.CharField(max_length=100)
    designation_code = models.CharField(max_length=10)
    status = models.BooleanField(default=True)

class AmsQualification(models.Model):
    qualification_name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)

class AmsDivision(models.Model):
    division_name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)

class AmsEmployeeCategory(models.Model):
    
    

    EMPLOYEE_TYPE_CHOICES = [
        (1, 'Accountant'),
        (2, 'Teacher'),
        (3, 'Librarian'),
        (4, 'Cafeteria'),
        (5, 'Other'),
    ]

    employee_category_name = models.CharField(max_length=255)
    employee_category_area = models.IntegerField(choices=EMPLOYEE_TYPE_CHOICES)
    status = models.BooleanField(default=True)

class AmsSubject(models.Model):
    subject_name = models.CharField(max_length=150)
    class_name = models.ManyToManyField('AmsClass')
    status = models.BooleanField(default=True)
