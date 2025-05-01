from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView
from .models import Task, Category, SubTask
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'tasks/index.html'
    model = Task

    def get_context_data(self, *args, **kwargs):
        today = timezone.now().date().day
        context = super().get_context_data(*args, **kwargs)
        context['uncompleted'] = Task.objects.filter(Q(completed=False) & Q(user=self.request.user))
        context['completed'] = Task.objects.filter(Q(completed=True) & Q(user=self.request.user) & Q(when_completed__day = today))
        context['counter'] = context['completed'].count() + context['uncompleted'].count()
        context['categories'] = Category.objects.filter(Q(user=self.request.user) | Q(high_p=True))
        context['high_p_tasks'] = Task.objects.filter(Q(user=self.request.user) & Q(category__high_p = True))
        return context


def add_category(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        if name:
            Category.objects.create(title=name, user=request.user)
    return redirect("index")


def end_task(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.completed = True
        task.when_completed = timezone.now()
        task.end_time = timezone.now()
        task.save()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(['POST'])


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        start_time = timezone.now()
        user = request.user
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id) if category_id else None

        Task.objects.create(user=user, title=title, category=category, start_time=start_time)
    return redirect('index')


class DetailTaskView(DetailView, LoginRequiredMixin):
    template_name = 'tasks/detail.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtasks'] = SubTask.objects.filter(task=self.object)
        return context

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('index')

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        new_title = request.POST.get('title', '').strip()
        if new_title:
            task.title = new_title
            task.save()
    return redirect('detail', pk=pk)

class SindexView(TemplateView):
    template_name = 'tasks/sindex.html'


def fbv_registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    return render(request, 'tasks/register.html', context={'form': form})




