from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, PracticeSession

@login_required
def practice_home(request):
    questions = Question.objects.all()
    return render(request, 'practice/home.html', {'questions': questions})
    # ... (rest of the view logic)

@login_required
def question_details(request,pk):
    question = get_object_or_404(Question, pk=pk)

    if request.method == "POST":
        selected_answer = request.POST.get('answer')
        is_correct = question.correct_answer.filter(answer_text = selected_answer, is_correct=True).exists()
        return render(request, 'practice/question_details.html',
                      {'question': question,
                       'is_correct': is_correct,
                       'selected_answer': selected_answer})

    return render(request, 'practice/question_detail.html', {'question': question})

def session_summary(request):
    user_sessions = PracticeSession.objects.filter(user=request.user)
    return render(request, 'practice/session_summary.html', {'sessions': user_sessions})
    # ... (logic to process user answers and calculate score)