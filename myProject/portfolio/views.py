from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Portfolio Home Page!")

def about(request):
    a = 10
    b = 20
    c = a + b
    return HttpResponse(f"The sum of {a} and {b} is {c}.")
