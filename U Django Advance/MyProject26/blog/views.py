from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_cookies(request):
    response = HttpResponse('Cookies Set Successfully!')
    response.set_cookie('username','Aryan Tomar', max_age=60*60*24*7) # cookies are valid for 7 days
    response.set_cookie('course','Django Full Course', max_age=60*60*24) # cookies are valid for 1 days
    return response


def get_cookies(request):
    username = request.COOKIES.get('username','Guest')
    course = request.COOKIES.get('course', 'No Course Selected')
    # return HttpResponse(f"Welcome {username}, you are enrolled in {course}.")
    if 'username' in request.COOKIES:
        return HttpResponse(f"Welcome {username}, you are enrolled in {course}.")
    else:
        return HttpResponse("No Course Selected")

def delete_cookies(request):
    response = HttpResponse("The cookies has been deleted")
    response.delete_cookie('username')
    response.delete_cookie('course')
    return response