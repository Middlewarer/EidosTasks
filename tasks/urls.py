from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('complete/<int:pk>/', views.end_task, name='complete_task'),
    path('add_task/', views.add_task, name='add_task'),
    path('detail/<int:pk>/', views.DetailTaskView.as_view(), name='detail'),
]