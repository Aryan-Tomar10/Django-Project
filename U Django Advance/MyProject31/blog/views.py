from django.shortcuts import render
from .models import UserProfile
from django.core.cache import cache

# Create your views here.
def user_profile_view(request):
    user_data = cache.get('user_data')
    if user_data is None:
        print('Fetching data from database')
        user_data = UserProfile.objects.all()
        cache.set('user_data',user_data)
    else:
        print('Fetching data from cache')
    return render(request,'user_profile.html',{'users': user_data})