from django.shortcuts import render
from .models import AmsClass,AmsDepartment,AmsDesignation,AmsQualification,AmsDivision,AmsEmployeeCategory
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings


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
        elif not department_code:
            messages.error(request, 'Department code cannot be blank.')
        elif AmsDepartment.objects.filter(department_code=department_code).exists():
            messages.error(request, 'Department with this code already exists.')
        else:
            AmsDepartment.objects.create(
                department_name=department_name,
                department_code=department_code
            )
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
            AmsDesignation.objects.create(
                designation_name=designation_name, 
                designation_code=designation_code
                )
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



def admin_employee_category(request):
    employees = AmsEmployeeCategory.objects.all()

    if request.method == 'POST':
        employee_category_name = request.POST.get('category_name', '').strip()
        employee_category_area = request.POST.get('category_area', '').strip()

        if not employee_category_name or not employee_category_area:
            messages.error(request, 'Both Employee Name and Area are required.')
        elif AmsEmployeeCategory.objects.filter(employee_category_name__iexact=employee_category_name).exists():
            messages.error(request, 'Employee Name already exists.')
        elif AmsEmployeeCategory.objects.exclude(employee_category_area=5).filter(employee_category_area=employee_category_area).exists():
            messages.error(request, 'Employee Area already exists.')
        else:
            AmsEmployeeCategory.objects.create(
                employee_category_name=employee_category_name,
                employee_category_area=employee_category_area
            )
            messages.success(request, 'Employee added successfully.')

    return render(request, 'admin_master_employee_category_manage.html', {"settings": settings,'employee':employees})






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




def ajax_department_view(request):
        department_id = request.GET['id']
        response_data = AmsDepartment.objects.get(id=department_id)
        serialized_data= {
            'department_name': response_data.department_name,
            'department_code': response_data.department_code,
            'status':1 if response_data.status else 0,

        }
        return JsonResponse(serialized_data)

def ajax_employee_category_view(request):
    if request.method == 'GET':
        try:
            category_id = request.GET['id']
            response_data = AmsEmployeeCategory.objects.get(id=category_id)

            serialized_data = {
                'employee_category_name': response_data.employee_category_name,
                'employee_category_area': response_data.employee_category_area,
                'status': 1 if response_data.status else 0,
            }

            return JsonResponse(serialized_data)

        except AmsEmployeeCategory.DoesNotExist:
            return JsonResponse({'error': 'Invalid employee category ID', 'success': ''})
    else:
        return JsonResponse({'error': 'Invalid request method', 'success': ''})


def ajax_designation_view(request):
    designation_id = request.GET['id']
    response_data = AmsDesignation.objects.get(id=designation_id)
    serialized_data = {
        'designation_name': response_data.designation_name,
        'designation_code': response_data.designation_code,
        'status': 1 if response_data.status else 0,
    }
    return JsonResponse(serialized_data)

def ajax_division_view(request):
    division_id = request.GET['id']
    response_data = AmsDivision.objects.get(id=division_id)  # Update to your actual model name
    serialized_data = {
        'division_name': response_data.division_name,
        'status': 1 if response_data.status else 0,
    }
    return JsonResponse(serialized_data)
def ajax_qualification_view(request):
    qualification_id = request.GET['id']
    response_data = AmsQualification.objects.get(id=qualification_id)  # Update to your actual model name
    serialized_data = {
        'qualification_name': response_data.qualification_name,  # Update to your actual model name
        'status': 1 if response_data.status else 0,
    }
    return JsonResponse(serialized_data)
def ajax_class_view(request):
    class_id = request.GET['id']
    response_data = AmsClass.objects.get(id=class_id)  # Update to your actual model name
    serialized_data = {
        'class_name': response_data.class_name,  # Update to your actual model name
        'status': 1 if response_data.status else 0,
    }
    return JsonResponse(serialized_data)


def ajax_department_update(request):
    if request.method == 'GET':
        try:
            department_id = request.GET['id']
            department_name = request.GET['department_name']
            department_code = request.GET['department_code']
            status = request.GET['status']

            ams_department = AmsDepartment.objects.get(id=department_id)

            if not department_name:
                return JsonResponse({'error': 'Department name cannot be blank.','success':''})
            elif AmsDepartment.objects.exclude(id=department_id).filter(department_name=department_name).exists():
                return JsonResponse({'error': 'Department with this name already exists.','success':''})
            elif not department_code:
                return JsonResponse({'error': 'Department code cannot be blank.'})
            elif AmsDepartment.objects.exclude(id=department_id).filter(department_code=department_code).exists():
                return JsonResponse({'error': 'Department with this code already exists.','success':''})
            else:
                # Update department
                ams_department.department_name = department_name
                ams_department.department_code = department_code
                ams_department.status = status

                ams_department.save()

            return JsonResponse({'success': 'Department updated successfully.','error':''})

        except AmsDepartment.DoesNotExist:
            return JsonResponse({'error': 'Invalid department ID','success':''})
    else:
        return JsonResponse({'error': 'Invalid request method', 'success': '','success':''})

def ajax_designation_update(request):
    if request.method == 'GET':
        try:
            designation_id = request.GET['id']
            designation_name = request.GET['designation_name']
            designation_code = request.GET['designation_code']
            status = request.GET['status']

            ams_designation = AmsDesignation.objects.get(id=designation_id)

            if not designation_name:
                return JsonResponse({'error': 'Designation name cannot be blank.', 'success': ''})
            elif AmsDesignation.objects.exclude(id=designation_id).filter(designation_name=designation_name).exists():
                return JsonResponse({'error': 'Designation with this name already exists.', 'success': ''})
            elif not designation_code:
                return JsonResponse({'error': 'Designation code cannot be blank.', 'success': ''})
            elif AmsDesignation.objects.exclude(id=designation_id).filter(designation_code=designation_code).exists():
                return JsonResponse({'error': 'Designation with this code already exists.', 'success': ''})
            else:
                # Update designation
                ams_designation.designation_name = designation_name
                ams_designation.designation_code = designation_code
                ams_designation.status = status

                ams_designation.save()

            return JsonResponse({'success': 'Designation updated successfully.', 'error': ''})

        except AmsDesignation.DoesNotExist:
            return JsonResponse({'error': 'Invalid designation ID', 'success': ''})
    else:
        return JsonResponse({'error': 'Invalid request method', 'success': '', 'success': ''})

def ajax_division_update(request):
    if request.method == 'GET':
        try:
            division_id = request.GET['id']
            division_name = request.GET['division_name']
            status = request.GET['status']

            ams_division = AmsDivision.objects.get(id=division_id)

            if not division_name:
                return JsonResponse({'error': 'Division name cannot be blank.', 'success': ''})
            elif AmsDivision.objects.exclude(id=division_id).filter(division_name=division_name).exists():
                return JsonResponse({'error': 'Division with this name already exists.', 'success': ''})
            else:
                # Update division
                ams_division.division_name = division_name
                ams_division.status = status

                ams_division.save()

            return JsonResponse({'success': 'Division updated successfully.', 'error': ''})

        except AmsDivision.DoesNotExist:
            return JsonResponse({'error': 'Invalid division ID', 'success': ''})
    else:
        return JsonResponse({'error': 'Invalid request method', 'success': ''})

def ajax_qualification_update(request):
    if request.method == 'GET':
        try:
            qualification_id = request.GET['id']
            qualification_name = request.GET['qualification_name']
            status = request.GET['status']

            ams_qualification = AmsQualification.objects.get(id=qualification_id)  # Update to your actual model name

            if not qualification_name:
                return JsonResponse({'error': 'Qualification name cannot be blank.', 'success': ''})
            elif AmsQualification.objects.exclude(id=qualification_id).filter(qualification_name=qualification_name).exists():  # Update to your actual model name
                return JsonResponse({'error': 'Qualification with this name already exists.', 'success': ''})
            else:
                # Update qualification
                ams_qualification.qualification_name = qualification_name  # Update to your actual model name
                ams_qualification.status = status

                ams_qualification.save()

            return JsonResponse({'success': 'Qualification updated successfully.', 'error': ''})

        except AmsQualification.DoesNotExist:  # Update to your actual model name
            return JsonResponse({'error': 'Invalid qualification ID', 'success': ''})
    else:
        return JsonResponse({'error': 'Invalid request method', 'success': ''})



def ajax_employee_category_update(request):
    if request.method == 'GET':
        try:
            category_id = request.GET['id']
            category_name = request.GET['category_name']
            category_area = request.GET['category_area']
            status = request.GET['status']

            # Fetch the category object
            employee_category = AmsEmployeeCategory.objects.get(id=category_id)

            # Check if the new name is blank or already exists
            if not category_name:
                return JsonResponse({'error': 'Employee Name cannot be blank.', 'success': ''})
            elif AmsEmployeeCategory.objects.exclude(id=category_id).filter(employee_category_name__iexact=category_name).exists():
                return JsonResponse({'error': 'Employee Name already exists.', 'success': ''})

            # Check if the new area is blank or already exists
            elif not category_area:
                return JsonResponse({'error': 'Employee Area cannot be blank.', 'success': ''})
            elif AmsEmployeeCategory.objects.exclude(id=category_id).filter(employee_category_area=category_area).exists():
                return JsonResponse({'error': 'Employee Area already exists.', 'success': ''})
            else:
                # Update the category
                employee_category.employee_category_name = category_name
                employee_category.employee_category_area = category_area
                employee_category.status = status

                # Save the changes
                employee_category.save()

                return JsonResponse({'success': 'Category updated successfully.', 'error': ''})

        except AmsEmployeeCategory.DoesNotExist:
            return JsonResponse({'error': 'Invalid category ID', 'success': ''})
    else:
        return JsonResponse({'error': 'Invalid request method', 'success': ''})


def ajax_class_update(request):
    if request.method == 'GET':
        try:
            class_id = request.GET['id']
            class_name = request.GET['class_name']
            status = request.GET['status']

            ams_class = AmsClass.objects.get(id=class_id)  # Update to your actual model name

            if not class_name:
                return JsonResponse({'error': 'Class name cannot be blank.', 'success': ''})
            elif AmsClass.objects.exclude(id=class_id).filter(class_name=class_name).exists():  # Update to your actual model name
                return JsonResponse({'error': 'Class with this name already exists.', 'success': ''})
            else:
                # Update class
                ams_class.class_name = class_name  # Update to your actual model name
                ams_class.status = status

                ams_class.save()

            return JsonResponse({'success': 'Class updated successfully.', 'error': ''})

        except AmsClass.DoesNotExist:  # Update to your actual model name
            return JsonResponse({'error': 'Invalid class ID', 'success': ''})
    else:
        return JsonResponse({'error': 'Invalid request method', 'success': ''})


def ajax_delete_row1(request):
    if request.method == 'GET':
        department_id = request.GET['id']
        try:
            # Assuming your model has a 'status' field
            row = AmsDepartment.objects.get(id=department_id)
            row.delete()

            return JsonResponse({'success': 'Row deleted successfully.','error':''})
        except AmsDepartment.DoesNotExist:
            return JsonResponse({'error': 'Invalid row ID.','success':''})
    else:
        return JsonResponse({'error': 'Invalid request method.','success':''})
    
def ajax_delete_desrow1(request):
    if request.method == 'GET':
        designation_id = request.GET['id']
        try:
            # Assuming your model has a 'status' field
            row = AmsDesignation.objects.get(id=designation_id)
            row.delete()

            return JsonResponse({'success': 'Row deleted successfully.','error':''})
        except AmsDesignation.DoesNotExist:
            return JsonResponse({'error': 'Invalid row ID.','success':''})
    else:
        return JsonResponse({'error': 'Invalid request method.','success':''})
    
def ajax_delete_divsrow(request):
    if request.method == 'GET':
        division_id = request.GET['id']
        try:
            # Assuming your model has a 'status' field
            row = AmsDivision.objects.get(id=division_id)  # Update to your actual model name
            row.delete()

            return JsonResponse({'success': 'Row deleted successfully.', 'error': ''})
        except AmsDivision.DoesNotExist:  # Update to your actual model name
            return JsonResponse({'error': 'Invalid row ID.', 'success': ''})
    else:
        return JsonResponse({'error': 'Invalid request method.', 'success': ''})


def ajax_delete_qualification_row(request):
    if request.method == 'GET':
        qualification_id = request.GET['id']
        try:
            # Assuming your model has a 'status' field
            row = AmsQualification.objects.get(id=qualification_id)  # Update to your actual model name
            row.delete()

            return JsonResponse({'success': 'Row deleted successfully.', 'error': ''})
        except AmsQualification.DoesNotExist:  # Update to your actual model name
            return JsonResponse({'error': 'Invalid row ID.', 'success': ''})
    else:
        return JsonResponse({'error': 'Invalid request method.', 'success': ''})
def ajax_delete_class_row(request):
    if request.method == 'GET':
        class_id = request.GET['id']
        try:
            # Assuming your model has a 'status' field
            row = AmsClass.objects.get(id=class_id)  # Update to your actual model name
            row.delete()

            return JsonResponse({'success': 'Row deleted successfully.', 'error': ''})
        except AmsClass.DoesNotExist:  # Update to your actual model name
            return JsonResponse({'error': 'Invalid row ID.', 'success': ''})
    else:
        return JsonResponse({'error': 'Invalid request method.', 'success': ''})


def ajax_delete_employee_row(request):
    if request.method == 'GET':
        employee_id = request.GET['id']
        try:
            # Assuming your model has a 'status' field
            row = AmsEmployeeCategory.objects.get(id=employee_id)  # Update to your actual model name
            row.delete()

            return JsonResponse({'success': 'Row deleted successfully.', 'error': ''})
        except AmsEmployeeCategory.DoesNotExist:  # Update to your actual model name
            return JsonResponse({'error': 'Invalid row ID.', 'success': ''})
    else:
        return JsonResponse({'error': 'Invalid request method.', 'success': ''})
