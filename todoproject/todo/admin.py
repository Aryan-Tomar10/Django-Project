from django.contrib import admin
from .models import TASK

# Register your models here.
@admin.register(TASK)
class TASK_ADMIN(admin.ModelAdmin):
    list_display = ('title','description','created_at')
    list_filter = ('completed','created_at')
    search_fields = ('title','description')
    ordering = ('-created_at',)
