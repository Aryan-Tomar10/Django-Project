from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_session(request):
    request.session['username'] = 'Aryan'
    request.session['course'] = 'Django Full Course'
    return HttpResponse("Session data saved successfully")

def get_session(request):
    username = request.session.get('username','Guest')
    course = request.session.get('course','Not Enrolled')
    return HttpResponse(f"Welcome : {username}, You are learning : {course}")

# def delete_session(request):
#     try:
#         del request.session['username']
#         del request.session['course']
#     except KeyError:
#         pass
#     return HttpResponse("Session data deleted successfully")

def delete_session(request):
    request.session.flush() # This will delete all the session data
    return HttpResponse("Session data deleted successfully")