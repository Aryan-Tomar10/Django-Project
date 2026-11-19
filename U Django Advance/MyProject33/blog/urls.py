from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name = 'users'),
    path('clear/', views.clear_cache, name = 'clear_cache')
]
