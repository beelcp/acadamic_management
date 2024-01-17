from django.shortcuts import render,get_object_or_404
from django.conf import settings
from admin_master.models import AmsClass, AmsQualification, AmsDivision, AmsDepartment, AmsDesignation, AmsEmployeeCategory, AmsSubject
from .models import Adminemp, employeedesignation, employeedpepartment, salary, subjectclassdivision
from django.http import JsonResponse
import json
import qrcode
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

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

                                                    





def get_subjects(request):
    class_id = request.GET['classId']
    academic_class = get_object_or_404(AmsClass, id=class_id, status=True)
    subjects = list(AmsSubject.objects.filter(class_name=academic_class, status=True).values('id', 'subject_name'))
    print(subjects)
    response_data={"subjects":subjects}
    return JsonResponse(response_data)

    # Handle invalid requests


def admin_employee_adddbms(request):
    qualification_data = AmsQualification.objects.filter(status=True)
    designation_data = AmsDesignation.objects.filter(status=True)
    department_data = AmsDepartment.objects.filter(status=True)
    employee_data = AmsEmployeeCategory.objects.filter(status=True)
    class_data = AmsClass.objects.filter(status=True)
    division_data = AmsDivision.objects.filter(status=True)
    subject_data = AmsSubject.objects.filter(status=True)

    

    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        dob = request.POST.get('dateofbirth')
        department = request.POST.get('department')
        jdate = request.POST.get('joiningdate')

        # qr_data = f"Name: {fname} {lname}\nDOB: {dob}\nDepartment: {department}\nJoin Date: {jdate}"
        qr_data = f"Name: {fname} {lname}\nDOB: {dob}\nDepartment: {department}\nJoin Date: {jdate}\nPhoto: {request.FILES.get('photo')}\nQualification: {AmsQualification.objects.get(id=request.POST.get('qualification')).qualification_name}"


        # Generate QR code image
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image to a BytesIO object
        qr_image_io = BytesIO()
        img.save(qr_image_io, format='PNG')
        qr_image_io.seek(0)

        # Create an InMemoryUploadedFile from BytesIO
        qr_image = InMemoryUploadedFile(
            file=qr_image_io,
            field_name=None,
            name=f'qr_code_{fname}_{lname}.png',
            content_type='image/png',
            size=qr_image_io.tell(),
            charset=None,
        )
        catlst=request.POST.get('employeecategory')
        catlss=catlst.split("+")
        qualification = AmsQualification.objects.get(id=request.POST.get('qualification'))
        designation = AmsDesignation.objects.get(id=request.POST.get('designation'))
        department_instance = AmsDepartment.objects.get(id=request.POST.get('department'))
        employee_category = AmsEmployeeCategory.objects.get(id=catlss[0])

        employee = Adminemp.objects.create(
            # employee_category_id=Adminemp.objects.select_related('employeecategory').all(),
            # employee_category_id=AmsEmployeeCategory.objects.get(id=request.POST.get('employee_category')),
            employee_category_id=employee_category,
            employee_category_name=fname + ' ' + lname,
            date_of_birth=dob,
            mobile=request.POST.get('phone'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            join_date=jdate,
            photo=request.FILES.get('photo'),
            qualification_id=qualification,
            designation_id=designation,
            department_id=department_instance,
            salary=request.POST.get('salaryamount'),
            gender=request.POST.get('gender'),
            barcode=qr_image,
        )


        # Handle employeedesignation
        employeedesignation.objects.create(
            employee_category_id=employee,
            designation_id=designation,
            from_date=jdate,
        )

        # Handle employeedpepartment
        employeedpepartment.objects.create(
            employee_category_id=employee,
            department_id=department_instance,
            from_date=jdate,
        )

        # Handle salary
        salary.objects.create(
            employee_category_id=employee,
            salary=request.POST.get('salaryamount'),
            from_date=jdate,
        )

    

        class_ids = request.POST.getlist('class_ids[]')
        division_ids = request.POST.getlist('division_ids[]')
        subject_ids = request.POST.getlist('subject_ids[]')

        for class_id, division_id, subject_id in zip(class_ids, division_ids, subject_ids):
            subjectclassdivision.objects.create(
                employee_category_id=employee,
                class_id=AmsClass.objects.get(id=class_id),
                division_id=AmsDivision.objects.get(id=division_id),
                subject_id=AmsSubject.objects.get(id=subject_id),
            )

    context = {
        'qualification_data': qualification_data,
        'designation_data': designation_data,
        'department_data': department_data,
        'employee_data': employee_data,
        'class_data': class_data,
        'division_data': division_data,
        'subject_data': subject_data,
    }
    return render(request, "admin_employee_add.html", context)




def admin_employee_list(request):
    adminemp_list = Adminemp.objects.all()
    return render(request, 'admin_employee_list.html', {'adminemp_list': adminemp_list})
