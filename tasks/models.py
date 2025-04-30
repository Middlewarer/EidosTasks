from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User

def date_validation(value):
    if value < timezone.now():
        raise ValidationError('Нельзя назначить дату дедлайна в прошлое')

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    when_completed = models.DateField(null=True, blank=True, default=timezone.now())
    due_date = models.DateTimeField(validators=[date_validation], null=True, blank=True)

    def __str__(self):
        return self.title
