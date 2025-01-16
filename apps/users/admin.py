from django.contrib import admin
from apps.users.models import CustomUser

@admin.register(CustomUser)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email','role', 'is_student_field', 'is_instructor_field']
    search_fields = ['username', 'email']
    list_filter = ['role', 'is_student_field','is_instructor_field']