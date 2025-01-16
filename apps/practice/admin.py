from django.contrib import admin
from .models import Question, UserAnswer, PracticeSession

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'date_taken']

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['practice_session','question', 'answer_given', 'is_correct'] #added session
    list_filter = ['is_correct', 'practice_session__started_at'] #added filter

@admin.register(PracticeSession)
class PracticeSessionAdmin(admin.ModelAdmin):
    list_display = ['user', 'started_at', 'completed_at', 'score']
    readonly_fields = ['score'] #added readonly
    list_filter = ['user', 'started_at'] #added filter