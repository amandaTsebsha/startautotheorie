from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, UserAnswer, PracticeSession
from django.contrib import messages
from django.utils import timezone

def index(request):
    return render(request, 'users/index.html')

def bestel(request):
    return render(request, 'users/bestel.html')

def faq(request):
    return render(request, 'users/faq.html')

def contact(request):
    return render(request, 'users/contact.html')

@login_required
def practice_home(request):
    if request.method == "POST":
        answers = request.POST
        practice_session = PracticeSession.objects.create(user=request.user)
        correct_count = 0

        for question_id, answer in answers.items():
            if question_id.startswith("question_"):
                try:
                    question_id = int(question_id.split("_")[1]) #convert to int
                    question = Question.objects.get(pk=question_id)
                    is_correct = answer == question.correct_answer
                    UserAnswer.objects.create(practice_session=practice_session, question=question, answer_given=answer, is_correct=is_correct)
                    if is_correct:
                        correct_count += 1
                except (Question.DoesNotExist, ValueError): #handle errors
                     messages.error(request, "Invalid question data submitted.")
                     practice_session.delete()
                     return redirect('users:users') # Redirect to prevent incomplete session

        practice_session.score = correct_count
        practice_session.completed_at = timezone.now()
        practice_session.save()
        messages.success(request, "Answers submitted!")
        return redirect('users:session_summary')

    questions = Question.objects.all()
    return render(request, 'users/home.html', {'questions': questions})

@login_required
def question_details(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        selected_answer = request.POST.get('answer')
        is_correct = selected_answer == question.correct_answer
        return render(request, 'users/question_details.html', {'question': question, 'is_correct': is_correct, 'selected_answer': selected_answer})
    return render(request, 'users/question_details.html', {'question': question}) # Consistent template name

@login_required
def session_summary(request):
    try:
        latest_session = PracticeSession.objects.filter(user=request.user).latest('started_at')
        user_answers = UserAnswer.objects.filter(practice_session=latest_session)
        total_questions = user_answers.count()
        correct_answers = user_answers.filter(is_correct=True).count()
        score_percentage = (correct_answers / total_questions * 100) if total_questions > 0 else 0
        return render(request, "users/results.html", {
            "user_answers": user_answers,
            "total_questions": total_questions,
            "correct_answers": correct_answers,
            "score_percentage": score_percentage,
            "session": latest_session
        })
    except PracticeSession.DoesNotExist:
        messages.info(request, "You haven't completed any users sessions yet.") #inform user
        return redirect('users:users')