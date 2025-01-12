from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

class CustomLoginView(LoginView):
    template_name = 'users/login.html'  #Double check Directory

    def get_success_url(self):
        return self.request.GET.get('next', '/')


class CustomLogoutView(LogoutView):
    next_page = '/'

