from django.contrib import admin
from .models import YouTubeUser
from django.core.cache import cache
from django.contrib import messages # to clear cache from admin panel

@admin.action(description='Clear Users Cache')
def clear_users_cache(modeladmin, request, queryset):
    cache.delete('user_data')
    messages.success(request,"User Cache cleared successfully.")

# Register your models here.
@admin.register(YouTubeUser)
class YouTubeUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscribers')
    actions = [clear_users_cache]  # to clear cache from admin panel