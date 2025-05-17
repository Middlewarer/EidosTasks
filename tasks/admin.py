from django.contrib import admin
from .models import Task, Category, SubTask, Example

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(SubTask)
admin.site.register(Example)

# Register your models here.
