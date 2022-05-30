from django.shortcuts import redirect, render

from adminapp.models import Student
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/adminapp/login')
def student_home(request):
    student=request.user.Student
    context = {
        "is_home": True,
        "student":student,
        }
    return render(request,'student/student_home.html',context)


@login_required(login_url='/adminapp/login')
def profile(request):
    student=request.user.Student
    student_profile=Student.objects.get(id=request.user.Student.id)
    context = {
        "is_profile": True,
        "student":student,
        "student_profile":student_profile,
        }
    return render(request,'student/profile.html',context)


@login_required(login_url='/adminapp/login')
def edit_profile(request,cid):
    student=request.user.Student
    if request.method == "POST":
        if 'id' in request.POST:
            id=request.POST['id']
            first_name=request.POST['fname']
            second_name=request.POST['sname']
            gender=request.POST['gender']
            dob=request.POST['dob']
            email=request.POST['email']
            phone=request.POST['phone']
            Student.objects.filter(id=cid).update(student_id=id,first_name=first_name,last_name=second_name,gender=gender,dob=dob,phone=phone,email=email)
            return redirect('student:profile')
        # elif 'fname' in request.POST:
        #     fname=request.POST['fname']
        #     fatherphone=request.POST['fatherhone']
        #     address=request.POST['address']
        #     Student.objects.filter(id=cid).update(fathername=fname,fatherphone=fatherphone,address=address)
        #     return redirect('student:profile')
        elif 'cid' in request.POST:
            cid=request.POST['cid']
            cname=request.POST['cname']
            batch=request.POST['batch']
            duration=request.POST['duration']
            Student.objects.filter(id=cid).update(course__course__course_id=cid,course__course__couse_name=cname,course__course__Duration=duration,course__starting_date=batch)
            return redirect('student:profile')
            
    edit_profile=Student.objects.get(id=cid)
    context = {
        "is_editprofile": True,
        "edit_profile":edit_profile,
        "student":student
        }
    return render(request,'student/edit_profile.html',context)



def exam_list(request):
    student=request.user.Student
    context = {
        "is_examlist": True,
        "student":student
        }
    return render(request,'student/exam_list.html',context)



def exam_instructions(request):
    student=request.user.Student
    context = {
        "is_examinst": True,
        "student":student
        }
    return render(request,'student/exam_instructions.html',context)


def exam(request):
    student=request.user.Student
    context = {
        "is_exam": True,
        "student":student,
        }
    return render(request,'student/exam.html',context)

def examq(request):
    student=request.user.Student
    context = {
        "is_exam": True,
        "student":student,
        }
    return render(request,'student/examq.html',context)

def result(request):
    student=request.user.Student
    context = {
        "is_result": True,
        "student":student,
        }
    return render(request,'student/result.html',context)

def fee(request):
    student=request.user.Student
    context = {
        "is_fee": True,
        }
    return render(request,'student/fee.html',context)

def calendar(request):
    context = {
        "is_calendar": True,
        }
    return render(request,'student/calendar.html',context)