from django.shortcuts import render
from . models import Student


# Create your views here.
def student_list(request):
    student = Student.objects.all()
    return render(request,'portfolio/student_list.html',{'students' : student})