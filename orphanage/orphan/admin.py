from django.contrib import admin
from .models import Case,Help

# Register your models here.
@admin.register(Case)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'children', 'phone_number', 'email', 'address',  'situation']

@admin.register(Help)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'help_offered']