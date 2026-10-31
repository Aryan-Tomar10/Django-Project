from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base.html')

def blog(request):
    students_list = [
        {"name" : "Aryan", "class" : "10th"},
        {"name" : "Atharva", "class" : "9th"},
        {"name" : "Abhay", "class" : "8th"},
    ]
    return render(request,'blog.html',{'students': students_list})