from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from apps.users.models import CustomUser

class CustomLoginView(LoginView):
    template_name = 'users/templates/login.html'  #Double check Directory

    def get_success_url(self):
        return self.request.GET.get('next', '/')


class CustomLogoutView(LogoutView):
    next_page = '/'

