from django.contrib.auth.models import AbstractUser
from django.db import models

class UserChoices(models.TextChoices):
    STUDENT = 'student', 'Student'
    INSTRUCTOR = 'instructor', 'Instructor'

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=UserChoices.choices, default=UserChoices.STUDENT, verbose_name="Role")
    is_student_field = models.BooleanField(default=True, verbose_name="Is Student")  # New field
    is_instructor_field = models.BooleanField(default=False, verbose_name="Is Instructor")  # New field


    @property
    def is_instructor(self):
        return self.role == UserChoices.INSTRUCTOR

    @property
    def is_student(self):
        return self.role == UserChoices.STUDENT


    def save(self, *args, **kwargs):
        self.is_student_field = self.role == UserChoices.STUDENT
        self.is_instructor_field = self.role == UserChoices.INSTRUCTOR
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username