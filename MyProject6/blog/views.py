from django.shortcuts import render
from datetime import datetime
# Create your views here.

def blog_details(request):
    post = {
        'title' : 'My Second Blog',
        'Description' : 'Django is a high level Python web Framework',
        'author' : None,
        'created_at' : datetime(2026,12,1,15,31,13),
        'comment_count' : 5,
        'tags' : ['Django', 'Python', 'Web Framework']
    }
    return render(request,'blog/blog_details.html',{"post" : post})