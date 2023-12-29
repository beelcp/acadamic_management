from django.shortcuts import render
from .models import AmsClass,AmsDepartment,AmsDesignation,AmsQualification,AmsDivision
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.

def base(request):
    return render(request,'base.html')



def admin_department_manage(request):
    ams_departments = AmsDepartment.objects.all()

    if request.method == 'POST':
        department_name = request.POST.get('department_name', '').strip()
        department_code = request.POST.get('department_code', '').strip()

        if not department_name:
            messages.error(request, 'Department name cannot be blank.')
        elif AmsDepartment.objects.filter(department_name=department_name).exists():
            messages.error(request, 'Department with this name already exists.')
        else:
            AmsDepartment.objects.create(department_name=department_name, department_code=department_code)
            messages.success(request, 'Department created successfully.')

    return render(request, 'admin_master_department_manage.html', {'ams_departments': ams_departments})




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

        if not qualification_name:
            messages.error(request, 'Qualification name cannot be blank.')
        elif AmsQualification.objects.filter(qualification_name=qualification_name).exists():
            messages.error(request, 'Qualification with this name already exists.')
        else:
            AmsQualification.objects.create(qualification_name=qualification_name)
            messages.success(request, 'Qualification created successfully.')

    return render(request, 'admin_master_qualification_manage.html', {'ams_qualifications': ams_qualifications})






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


def admin_division_manage(request):
    ams_divisions = AmsDivision.objects.all()

    if request.method == 'POST':
        division_name = request.POST.get('division_name', '').strip()

        if not division_name:
            messages.error(request, 'Division name cannot be blank.')
        elif AmsDivision.objects.filter(division_name=division_name).exists():
            messages.error(request, 'Division with this name already exists.')
        else:
            AmsDivision.objects.create(division_name=division_name)
            messages.success(request, 'Division created successfully.')

    return render(request, 'admin_master_division_manage.html', {'ams_divisions': ams_divisions})


def admin_employee_category (request):
    return render(request,'admin_master_employee_category_manage.html')





def ajax_view(request):
    if request.method == 'POST' and request.is_ajax():
        id_param = request.POST.get('id', '')

        # Perform any necessary operations with the received data

        response_data = {
            'message': 'Success',
            'id': id_param,
            # Add other data as needed
        }

        return JsonResponse(response_data)
    else:
        # Handle non-AJAX requests, if needed
        return render(request, '')



# def ajax_department_view(request):
#     if request.method == 'GET' and request.is_ajax():
#         department_id = request.POST.get('id', '')

#         # Retrieve AmsDepartment object based on the 'id'
#         try:
#             department = AmsDepartment.objects.get(id=department_id)
#             response_data = {
#                 'message': 'Success',
#                 'department_name': department.department_name,
#                 'department_code': department.department_code,
#                 'status': department.status,
#                 # Add other data as needed
#             }
#         except AmsDepartment.DoesNotExist:
#             response_data = {'message': 'Department not found'}

#         return JsonResponse(response_data)
#     else:
#         # Handle non-AJAX requests, if needed
#         return render(request, 'your_template.html')
def ajax_department_view(request):
        department_id = request.GET['id']
        response_data = AmsDepartment.objects.get(id=department_id)
        serialized_data= {
            'department_name': response_data.department_name,
            'department_code': response_data.department_code,

        }
        return JsonResponse(serialized_data)



