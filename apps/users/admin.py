from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_student', 'is_instructor']
    search_fields = ['username', 'email']
    list_filter = ['is_student','is_instructor']