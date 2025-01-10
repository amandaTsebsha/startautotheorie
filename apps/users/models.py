from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomerUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_instructor = models.BooleanField(default=False, verbose_name="Is Instructor")
    is_student = models.BooleanField(default=True, verbose_name="Is Student")
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username