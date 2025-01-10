from django.db import models

class Question(models.Model):
    question_text = models.TextField()
    image_url = models.URLField(null=True, blank=True)  # For images
    options = models.JSONField()  # Store options as a JSON list
    correct_answer = models.CharField(max_length=255)
    explanation = models.TextField()

class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_given = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

class UserScore(models.Model):
    user = models.ForeignKey('users.CustomerUser', on_delete=models.CASCADE())
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)