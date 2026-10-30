from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog_details, name  = "blog_details")
]
