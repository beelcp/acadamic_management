from django.shortcuts import render
from admin_master.models import AmsClass,AmsDepartment,AmsDesignation,AmsQualification,AmsEmployeeCategory

# Create your views here.

def admin_employee_add(request):
    employee_designation=AmsDesignation.objects.all()
    employee_qualification=AmsQualification.objects.all()
    employee_category=AmsEmployeeCategory.objects.all()
    employee_department=AmsDepartment.objects.all()

    return render(request,'admin_employee_add.html',{'employee_des':employee_designation,'empl_qal':employee_qualification,                                                       'employee_dep':employee_department,
                    'employee_cat':employee_category,'employee_dep':employee_department, })

                                                    


    
