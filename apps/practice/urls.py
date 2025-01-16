from django.urls import path

from . import views
from .views import practice_home, question_details, session_summary

app_name = 'users'

urlpatterns = [
    path('', views.index, name='home'),
    path('bestel/', views.bestel, name='bestel'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('', practice_home, name='users'),
    path('question/<int:pk>/', question_details, name='question_details'),
    path('summary/', session_summary, name='session_summary'),
]