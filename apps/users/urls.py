from django.urls import path

from apps.practice.urls import app_name
from apps.users.views import CustomLoginView, CustomLogoutView

app_name = 'users'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]