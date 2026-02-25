from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    
    list_display = ('username', 'email', 'height', 'weight', 'fitness_goal', 'experience_level', 'is_staff')
    
  
    fieldsets = UserAdmin.fieldsets + (
        ('Fitness Bilgileri', {
            'fields': ('height', 'weight', 'fitness_goal', 'experience_level')
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)