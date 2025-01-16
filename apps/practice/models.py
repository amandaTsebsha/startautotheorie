from django.db import models
from django.conf import settings

class Question(models.Model):
    question_text = models.CharField(max_length=255, verbose_name="Vraagtekst")
    image_url = models.URLField(null=True, blank=True)
    options = models.JSONField()
    correct_answer = models.CharField(max_length=50, verbose_name="Correct Antwoord")
    date_taken = models.DateTimeField(auto_now_add=True)
    difficulty = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)]) #added difficulty

    def __str__(self):
        return self.question_text

class PracticeSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='practice_sessions')
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"Session by {self.user.username} at {self.started_at}"

class UserAnswer(models.Model):
    practice_session = models.ForeignKey(PracticeSession, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='user_answers')
    answer_given = models.CharField(max_length=255, verbose_name="Antwoordtekst")
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Answer to {self.question.id}: {self.answer_given} - {self.is_correct}"