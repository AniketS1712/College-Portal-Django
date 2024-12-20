from django.shortcuts import render, redirect, get_object_or_404
from academy.models import Students,faculty
from academy.forms import addinfo

def home_views(request):
    return render(request, 'academy/home.html',{})

def staff_views(request):
    return render(request,'academy/staff.html',{})

def staff_temlate_views(request,faculty_name):
    staff = get_object_or_404(faculty, F_Name = faculty_name)
    def staff_image(staff):
        if staff.F_Name == 'Dr. Ravish Sagar':
            return '../images_folder/director.PNG'
        elif staff.F_Name == 'Mr. Alok Mishra':
            return '../images_folder/alok_sir.PNG'
        elif staff.F_Name == 'Mr. Meetender':
            return '../images_folder/meetender_sir.jpg'
        elif staff.F_Name == 'Ms Gomathy M':
            return '../images_folder/gomathi_mam.PNG'
        elif staff.F_Name == 'Mr Akshit Thakur':
            return '../images_folder/akshit_sir.PNG'
        elif staff.F_Name == 'Ms. Sonia Batra':
            return '../images_folder/sonia_mam.PNG'
        elif staff.F_Name == 'Mr. Sandeep Jain':
            return '../images_folder/sandeep_sir.PNG'
        elif staff.F_Name == 'Dr. Sushma Bahuguna':
            return '../images_folder/sushma_mam.PNG'
        elif staff.F_Name == 'Dr. Anu Taneja':
            return '../images_folder/anu_mam.PNG'
        elif staff.F_Name == 'Ms. Smriti Sharma':
            return '../images_folder/smriti_mam.PNG'
        elif staff.F_Name == 'Ms. Mansi Vats':
            return '../images_folder/mansi__mam.jpg'
        elif staff.F_Name == 'Dr. Shalini Gambhir':
            return '../images_folder/shalini_mam.PNG'
    imagefile = staff_image(staff)
    return render(request,'academy/staff_template.html',{'data':[staff],'imgfile':imagefile})

def student_views(request):
    data = Students.objects.all()
    return render(request,'academy/student.html',{'student':data})

def add_info(request):
    if request.method == 'POST':
        form = addinfo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_views')
    else:
        form = addinfo()
    return render(request, 'academy/add_info_form.html', {'form': form})

def event_views(request):
    return render(request,'academy/event.html',{})
