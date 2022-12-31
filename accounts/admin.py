from django.contrib import admin

from .models import Department, Faculty, Profile


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'department']
    list_filter = ['department']
