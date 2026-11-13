from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail


@receiver(post_save, sender = User)
def send_welcome_email(sender,instance,created, **kwargs):
    if created:
        print(f"New User Created : {instance.username}")
        subject = "Welcome to Aryan Tomar."
        message = f"Hii {instance.username}, thankyou for regestering at Aryan Tomar Blog."
        from_email = 'aryantomar1005@gmail.com'
        recipient_list = [instance.email]

        send_mail(subject,message,from_email,recipient_list, fail_silently = False)
        print(f"Welcome email send to: {instance.email}")