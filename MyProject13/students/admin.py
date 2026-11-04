from django.contrib import admin
from .models import Student
# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','age','city')
    search_fields = ('name','city')
    list_filter = ('name','city','age')
    ordering = ('name',)