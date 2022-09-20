from django.contrib import admin

from .models import Event, Job


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location']
    prepopulated_fields = {'slug': ('title',)}
