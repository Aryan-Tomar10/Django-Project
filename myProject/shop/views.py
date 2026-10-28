from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Shopping Page")

def about(request):
    a = 30
    b = 40
    c = a + b
    return HttpResponse(f"The Price of {a} and {b} is {c}.")