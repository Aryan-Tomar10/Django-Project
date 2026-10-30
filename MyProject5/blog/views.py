from django.shortcuts import render
from datetime import datetime

# Create your views here.
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def home(request):
    context = {
        'name' : "Aryan Tomar",
        "age" : 23,
        "skill" : ["Python", "Django", "React"],
        "user" : User("Saloni", 22),
        "blog" : {
            "title" : "Django Title Intro",
            "content" : "<b>This is bold</b>",
            "created_at" : datetime(2026,10,22,10,20)
        },
        "empty_value" : None,
    }
    return render(request,"blog/home.html",context)