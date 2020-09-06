from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Batch
# Create your views here.


def home_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        if request.user.role == 'student' :
            return student_home_view(request, course, batch)
        else :
            return faculty_home_view(request, course, batch)
    else:
        return redirect('accounts/login')


def student_home_view(request, *args, **kwargs):
    # current users batch
    user_batch = request.user.batch
    return HttpResponse("<h1> student_home_view <h1>")

def faculty_home_view(request, *args, **kwargs):
    return HttpResponse("<h1> faculty_home_view <h1>")

def course_batch_view(request, course, batch):
    if request.user.is_authenticated :
        if request.user.role == 'student' :
            return student_course_batch_view(request, course, batch)
        else :
            return faculty_course_batch_view(request, course, batch)
    else :
        return redirect('accounts/login')
def student_course_batch_view(request, course, batch):
    return HttpResponse("<h1> student_course_batch_view <h1>")

def faculty_course_batch_view(request, course, batch):
    return HttpResponse("<h1> faculty_course_batch_view <h1>")


def add_lecture_view(request):
    if(request.method == 'GET'):
        return HttpResponse("<h1> Sorry you are unauthorized <h1>")
