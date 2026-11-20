from django.shortcuts import render
from .models import UserProfile
from django.core.cache import cache

# Create your views here.
def users_list(request):
    users = cache.get('user_list')
    if not users:
        print('Cache miss: querying database from users.')
        users = UserProfile.objects.all()
        cache.set('user_list', users, timeout = 60)
    else:
        print("cache hit")
    return render(request, 'userlist.html',{'users':users})