from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Task
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseNotAllowed


class IndexView(ListView):
    template_name = 'tasks/index.html'
    model = Task

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['uncompleted'] = Task.objects.filter(completed=False)
        context['completed'] = Task.objects.filter(completed=True)
        return context


def end_task(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.completed = True
        task.save()
        return redirect('index')  # вернуться назад
    else:
        return HttpResponseNotAllowed(['POST'])


def add_task(request):
    if request.method == 'POST':
        print('avoo')
        title = request.POST.get('title')
        if title:
            Task.objects.create(user=request.user, title=title)

    return redirect('index')


class DetailTaskView(DetailView):
    template_name = 'tasks/detail.html'
    model = Task