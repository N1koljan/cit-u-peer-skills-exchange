from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('school_id', 'department')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'department')

admin.site.register(CustomUser, CustomUserAdmin)