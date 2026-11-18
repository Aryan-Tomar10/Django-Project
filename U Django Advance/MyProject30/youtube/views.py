from django.shortcuts import render
from django.core.cache import cache
from .models import YouTubeUser

# Create your views here.
def users_list(request):
    users = cache.get('users_data')
    if not users:
        print("Catche miss : Fetching data from database")
        users = YouTubeUser.objects.all()
        cache.set('users_data',users,timeout=60)
    else:
        print("Catche hit : Fetching data from cache")
    return render(request,'user_list.html',{'users':users})