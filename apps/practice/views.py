from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, UserAnswer, PracticeSession

@login_required
def practice_home(request):

    if request.method == "GET":
        questions = Question.objects.all()
        return render(request, 'practice/home.html', {'questions': questions})

    if request.method == "POST":
        # Handle the submitted answers
        answers = request.POST
        for key, value in answers.items():
            if key.startswith("question_"):
                question_id = key.split("_")[1]
                question = Question.objects.get(id=question_id)
                is_correct = value == question.correct_answer
                UserAnswer.objects.create(
                    user=request.user,
                    question=question,
                    answer_given=value,
                    is_correct=is_correct,
                )
        return redirect('results')


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
    user_answers = UserAnswer.objects.filter(user=request.user)
    total_questions = user_answers.count()
    correct_answers = user_answers.filter(is_correct=True).count()
    score_percentage = (correct_answers / total_questions * 100) if total_questions > 0 else 0

    return render(request, "results.html", {
        "user_answers": user_answers,
        "total_questions": total_questions,
        "correct_answers": correct_answers,
        "score_percentage": score_percentage,
    })

    user_sessions = PracticeSession.objects.filter(user=request.user)
    return render(request, 'practice/session_summary.html', {'sessions': user_sessions})
    # ... (logic to process user answers and calculate score)