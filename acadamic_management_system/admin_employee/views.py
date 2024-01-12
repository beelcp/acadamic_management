from django.shortcuts import render,get_object_or_404
from admin_master.models import AmsClass,AmsDepartment,AmsDesignation,AmsQualification,AmsEmployeeCategory,AmsDivision,AmsSubject
from django.http import JsonResponse
from django.conf import settings

# Create your views here.

def admin_employee_add(request):
    employee_designation=AmsDesignation.objects.all()
    employee_qualification=AmsQualification.objects.all()
    employee_category=AmsEmployeeCategory.objects.all()
    employee_department=AmsDepartment.objects.all()
    employee_class=AmsClass.objects.all()
    employee_division=AmsDivision.objects.all()
    employee_subject=AmsSubject.objects.all()


    return render(request,'admin_employee_add.html',{'employee_des':employee_designation,'empl_qal':employee_qualification,'employee_dep':employee_department,
                    'employee_cat':employee_category,'employee_dep':employee_department,'employee_class':employee_class,'employee_division':employee_division,'employee_subject':employee_subject, })

                                                    


    

# def get_subjects(request):
#     # if request.method == 'GET' and request.is_ajax():
#         class_id = request.GET['classId']

#         # Query the subjects based on the selected class
#         subjects = AmsSubject.objects.filter(id=class_id,status=True).values('id', 'subject_name')

#         # Convert the queryset to a list of dictionaries
#         subjects_list = list(subjects)

#         return JsonResponse(subjects_list, safe=False)

#     # Handle invalid requests
#     # return JsonResponse({'error': 'Invalid request'}, status=400)



def get_subjects(request):
    class_id = request.GET['classId']
    academic_class = get_object_or_404(AmsClass, id=class_id, status=True)
    subjects = list(AmsSubject.objects.filter(class_name=academic_class, status=True).values('id', 'subject_name'))
    print(subjects)
    response_data={"subjects":subjects}
    return JsonResponse(response_data)

    # Handle invalid requests
