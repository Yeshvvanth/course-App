from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import CourseForm
from .models import courses
# Create your views here.


def course_list(request):
    course = courses.objects.all()
    return render(request,"course_list.html",{"courses":course})

def upload_courses(request):

    if request.method=="POST":
        form = CourseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request,"upload_course.html",{
        "form":form
    })

def delete_course(request,pk):
    if request.method == "POST":
        course = courses.objects.get(pk=pk)
        course.delete()
        return redirect('course_list')
