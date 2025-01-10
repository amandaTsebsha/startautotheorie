from django.shortcuts import render
from .models import Question, UserAnswer

def practice(request):
    questions = Question.objects.all()
    # ... (rest of the view logic)

def results(request):
    # ... (logic to process user answers and calculate score)