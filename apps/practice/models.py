from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=255, verbose_name="Vraagtekst")
    image_url = models.URLField(null=True, blank=True)  # For images
    options = models.JSONField()  # Store options as a JSON list
    correct_answer = models.CharField(max_length=50, verbose_name="Correct Antwoord")
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_given = models.CharField(max_length=255, verbose_name="Antwoordtekst")
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Answer to {self.question.id}: {self.answer_given} - {self.is_correct}"

class PracticeSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='practice_session')
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField()

    def __str__(self):
        return f"Session by {self.user.username} at {self.started_at}"
