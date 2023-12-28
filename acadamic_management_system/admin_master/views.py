from django.shortcuts import render
from .models import AmsClass,AmsDepartment,AmsDesignation,AmsQualification,AmsDivision
from django.contrib import messages


# Create your views here.

def base(request):
    return render(request,'base.html')



def admin_department_manage(request):
    ams_departments = AmsDepartment.objects.all()

    if request.method == 'POST':
        department_name = request.POST.get('department_name', '').strip()
        department_code = request.POST.get('department_code', '').strip()
        AmsDepartment.objects.create(department_name=department_name, department_code=department_code)

    return render(request, 'admin_master_department_manage.html', {'ams_departments': ams_departments})




# def admin_designation_manage(request):
#     ams_designations = AmsDesignation.objects.all()

#     if request.method == 'POST':
#         designation_name = request.POST.get('designation_name', '').strip()
#         designation_code = request.POST.get('designation_code', '').strip()
#         AmsDesignation.objects.create(designation_name=designation_name, designation_code=designation_code)

#     return render(request, 'admin_master_designation_manage.html', {'ams_designations': ams_designations})



def admin_designation_manage(request):
    ams_designations = AmsDesignation.objects.all()

    if request.method == 'POST':
        designation_name = request.POST.get('designation_name', '').strip()
        designation_code = request.POST.get('designation_code', '').strip()

        if not designation_name:
            messages.error(request, 'Designation name cannot be blank.')
        elif AmsDesignation.objects.filter(designation_name=designation_name).exists():
            messages.error(request, 'Designation with this name already exists.')
        elif not designation_code:
            messages.error(request, 'Designation code cannot be blank.')
        elif AmsDesignation.objects.filter(designation_code=designation_code).exists():
            messages.error(request, 'Designation with this code already exists.')
        else:
            AmsDesignation.objects.create(designation_name=designation_name, designation_code=designation_code)
            messages.success(request, 'Designation created successfully.')

    return render(request, 'admin_master_designation_manage.html', {'ams_designations': ams_designations})


def admin_qualification_manage(request):
    ams_qualifications = AmsQualification.objects.all()
    if request.method == 'POST':
        qualification_name = request.POST.get('qualification_name', '').strip()
        AmsQualification.objects.create(qualification_name=qualification_name)

    return render(request, 'admin_master_qualification_manage.html', {'ams_qualifications': ams_qualifications})


# def admin_class_manage (request):
#     ams_classes = AmsClass.objects.all()
#     if request.method == 'POST':
#         class_name = request.POST.get('class_name', '').strip()
#         AmsClass.objects.create(class_name=class_name)

#     return render(request, 'admin_master_class_manage.html', {'ams_classes': ams_classes})



def admin_class_manage(request):
    ams_classes = AmsClass.objects.all()

    if request.method == 'POST':
        class_name = request.POST.get('class_name', '').strip()

        if not class_name:
            # Handle the case where the input is blank
            messages.error(request, 'Class name cannot be blank.')
        elif AmsClass.objects.filter(class_name=class_name).exists():
            # Handle the case where the class name already exists
            messages.error(request, 'Class with this name already exists.')
        else:
            # Create a new instance
            AmsClass.objects.create(class_name=class_name)
            messages.error(request, 'added succecfully')

    return render(request, 'admin_master_class_manage.html', {'ams_classes': ams_classes})


# def admin_class_manage(request):
#     ams_classes = AmsClass.objects.all()

#     if request.method == 'POST':
#         class_name = request.POST.get('class_name', '').strip()

#         # Check if the input is not blank and a class with the same name doesn't exist
#         if class_name and not AmsClass.objects.filter(class_name=class_name).exists():
#             # Create a new instance
#             AmsClass.objects.create(class_name=class_name)
#         else:
#             # Handle the case where the input is blank or the class name already exists
#             # You can add an error message or take appropriate action
#             pass

#     return render(request, 'admin_master_class_manage.html', {'ams_classes': ams_classes})



def admin_division_manage(request):
    ams_divisions = AmsDivision.objects.all()

    if request.method == 'POST':
        division_name = request.POST.get('division_name', '').strip()
        AmsDivision.objects.create(division_name=division_name)

    return render(request, 'admin_master_division_manage.html', {'ams_divisions': ams_divisions})


def admin_employee_category (request):
    return render(request,'admin_master_employee_category_manage.html')


