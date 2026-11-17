from django.shortcuts import render
from django.http import HttpResponse
# from django.core.mail import send_mass_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.
# def send_bulk_email(request):
#     messages1 = ('Welcome user 1', 'Hello user 1 to our platform', 'aryantomar1005@gmail.com',['tomarmanju015@gmail.com'])
#     messages2 = ('Welcome user 1', 'Hello user 1 to our platform', 'aryantomar1005@gmail.com',['tomarmanju015@gmail.com'])
#     messages3 = ('Welcome user 1', 'Hello user 1 to our platform', 'aryantomar1005@gmail.com',['tomarmanju015@gmail.com'])
#     send_mass_mail((messages1,messages2,messages3),fail_silently=False)
#     return HttpResponse("Bulk email send successfully")


def send_bulk_email(request):
    subject = "Welcome to our Platform"
    from_email = "aryantomar1005@gmail.com"
    recipient_list = ['tomarmanju015@gmail.com', 'aryantomar10@icloud.com']
    html_content = render_to_string('Welcome_email.html',{'username':'Aryan'})
    msg = EmailMultiAlternatives(subject,"Welcome to my platform",from_email,recipient_list)
    # msg.attach_file('/Users/aryantomar/Downloads/AryanTomar_CV.pdf')
    msg.attach_alternative(html_content,'text/html')

    msg.send()
    return HttpResponse("Bulk email send successfully")