from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mass_mail

# Create your views here.
def send_bulk_email(request):
    messages1 = ('Welcome user 1', 'Hello user 1 to our platform', 'aryantomar1005@gmail.com',['tomarmanju015@gmail.com'])
    messages2 = ('Welcome user 1', 'Hello user 1 to our platform', 'aryantomar1005@gmail.com',['tomarmanju015@gmail.com'])
    messages3 = ('Welcome user 1', 'Hello user 1 to our platform', 'aryantomar1005@gmail.com',['tomarmanju015@gmail.com'])
    send_mass_mail((messages1,messages2,messages3),fail_silently=False)
    return HttpResponse("Bulk email send successfully")