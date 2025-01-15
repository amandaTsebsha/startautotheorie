from django.urls import path
from .views import practice_home, question_details, session_summary

app_name = 'practice'

urlpatterns = [
    path('', practice_home, name='practice'),
    path('question/<int:pk>/', question_details, name='question_details'),
    path('summary/', session_summary, name='session_summary'),
]