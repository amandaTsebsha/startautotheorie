from django.contrib import admin
from apps.practice.models import Question, UserAnswer, PracticeSession

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'date_taken']

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer_given', 'is_correct']

@admin.register(PracticeSession)
class PracticeSessionAdmin(admin.ModelAdmin):
    list_display = ['user', 'started_at', 'completed_at', 'score']
