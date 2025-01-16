from django.contrib.auth.models import AbstractUser
from django.db import models

class UserChoices(models.TextChoices):
    STUDENT = 'student', 'Student'
    INSTRUCTOR = 'instructor', 'Instructor'

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=UserChoices.choices, default=UserChoices.STUDENT, verbose_name="Role")

    @property
    def is_instructor(self):
        return self.role == UserChoices.INSTRUCTOR

    @property
    def is_student(self):
        return self.role == UserChoices.STUDENT

    def __str__(self):
        return self.username