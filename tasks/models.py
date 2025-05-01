from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User

def date_validation(value):
    if value < timezone.now():
        raise ValidationError('Нельзя назначить дату дедлайна в прошлое')

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    high_p = models.BooleanField(default=False)

    class Meta:
        ordering = ['-high_p', 'title']


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    when_completed = models.DateField(null=True, blank=True)
    due_date = models.DateTimeField(validators=[date_validation], null=True, blank=True)

    def duration(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time

    def __str__(self):
        return self.title

class SubTask(models.Model):
    title = models.CharField(max_length=255)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)



