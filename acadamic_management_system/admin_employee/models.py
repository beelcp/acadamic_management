from django.db import models
from admin_master.models import AmsClass, AmsDepartment, AmsDesignation, AmsDivision, AmsEmployeeCategory, AmsQualification, AmsSubject

class Adminemp(models.Model):
    employee_category_id=models.ForeignKey(AmsEmployeeCategory,on_delete=models.CASCADE)
    employee_category_name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    mobile=models.IntegerField(default=0)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    join_date=models.DateField()
    photo=models.ImageField(upload_to='employee_photos/',blank=True,null=True)
    qualification_id=models.ForeignKey(AmsQualification,on_delete=models.CASCADE)
    designation_id=models.ForeignKey(AmsDesignation,on_delete=models.CASCADE)
    department_id=models.ForeignKey(AmsDepartment,on_delete=models.CASCADE)
    salary=models.PositiveIntegerField()
    barcode=models.ImageField(upload_to='barcode/',blank=True,null=True)
    GENDER_CHOICES = [
        (0, 'Male'),
        (1, 'Female'), 
        (2, 'Other'),
    ]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    status=models.BooleanField(default=True)

class subjectclassdivision(models.Model):
    employee_category_id=models.ForeignKey(Adminemp,on_delete=models.CASCADE)
    class_id=models.ForeignKey(AmsClass,on_delete=models.CASCADE)
    division_id=models.ForeignKey(AmsDivision,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(AmsSubject,on_delete=models.CASCADE)


class employeedesignation(models.Model):
    employee_category_id=models.ForeignKey(Adminemp,on_delete=models.CASCADE)
    designation_id=models.ForeignKey(AmsDesignation,on_delete=models.CASCADE)
    from_date=models.DateField()
    to_date = models.DateTimeField(null=True, blank=True)


class employeedpepartment(models.Model):
    employee_category_id=models.ForeignKey(Adminemp,on_delete=models.CASCADE)
    department_id=models.ForeignKey(AmsDepartment,on_delete=models.CASCADE)
    from_date=models.DateField()
    to_date = models.DateTimeField(null=True, blank=True)


class salary(models.Model):
    employee_category_id = models.ForeignKey(Adminemp, on_delete=models.CASCADE, related_name='salaries')
    salary = models.PositiveIntegerField()
    from_date=models.DateField()
    to_date = models.DateTimeField(null=True, blank=True)



