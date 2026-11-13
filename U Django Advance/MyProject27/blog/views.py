from django.shortcuts import render
# from django.core.mail import send_mail,
from django.core.mail import  EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse

# Create your views here.
# # to send plane text mail
# def send_test_email(request):
#     subject = 'Welcome to my Blog'
#     message = 'This is a hacking message'
#     from_email = 'aryantomar1005@gmail.com'
#     recipient_list = ["tomarmanju015@gmail.com"]

#     send_mail(subject,message, from_email, recipient_list)
#     return HttpResponse("Test mail send successfully!")

# to send HTML mail
def send_test_email(request):
    subject = 'Welcome to my Blog'
    message = render_to_string('email/welcome_email.html',{
        'username': "Aryan",
        'course' : 'Django Tutorial'
    })
    email = EmailMessage(
        subject,
        message,
        "aryantomar1005@gmail.com",
        ["tomarmanju015@gmail.com"]
    )
    email.content_subtype = "html" # main content is now text/html
    email.send()
    return HttpResponse("Test mail send successfully!")