from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def show_msg(request):
    messages.debug(request,"This is a debug message") #Developer k lye
    messages.info(request, "This is a info message") #General info user k lye
    messages.success(request, "This is success message") #Positive action k lye
    messages.warning(request, "This is warning message") #Caution/ alert
    messages.error(request, "This is error message") #Action Failed/ error
    return render(request, 'message.html')