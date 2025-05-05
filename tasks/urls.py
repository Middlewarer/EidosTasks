from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('complete/<int:pk>/', views.end_task, name='complete_task'),
    path('add_task/', views.add_task, name='add_task'),
    path('detail/<int:pk>/', views.DetailTaskView.as_view(), name='detail'),
    path('detail/<int:pk>/update/', views.update_task, name='update_task'),
    path('detail/<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('login/', LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sindex/', views.SindexView.as_view(), name='sindex'),
    path('register/', views.fbv_registration, name='register'),
    path('add_category/', views.add_category, name='add_category'),
    path('tasks/', views.tasks_view, name='tasks')
]