from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.contrib.auth.views import LoginView
from .models import Task
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(ListView):
    template_name = 'tasks/index.html'
    model = Task

    def get_context_data(self, *args, **kwargs):
        today = timezone.now().date().day
        context = super().get_context_data(*args, **kwargs)
        context['uncompleted'] = Task.objects.filter(Q(completed=False) & Q(user=self.request.user))
        context['completed'] = Task.objects.filter(Q(completed=True) & Q(user=self.request.user) & Q(when_completed__day = today))
        context['counter'] = context['completed'].count() + context['uncompleted'].count()
        return context


def end_task(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.completed = True
        task.when_completed = timezone.now()
        task.save()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(['POST'])


def add_task(request):
    if request.method == 'POST':
        print('avoo')
        title = request.POST.get('title')
        if title:
            Task.objects.create(user=request.user, title=title)

    return redirect('index')


class DetailTaskView(DetailView, LoginRequiredMixin):
    template_name = 'tasks/detail.html'
    model = Task


class SindexView(TemplateView):
    template_name = 'tasks/sindex.html'



