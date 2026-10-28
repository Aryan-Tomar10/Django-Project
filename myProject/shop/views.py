from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def buy_detail(request,buy_id):
    return HttpResponse(f"<h1>Welcome to the Shopping Page : {buy_id}</h1>")


def user_profile(request,username):
    return HttpResponse(f"<h1>Profile of user : {username}</h1>")