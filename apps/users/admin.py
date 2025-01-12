from django.contrib import admin
from .models import CustomerUser


@admin.register(CustomerUser)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_student', 'is_instructor']