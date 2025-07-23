from django.urls import path
from . import views

urlpatterns = [
   path("", views.TaskListView.as_view(), name="task_list"),
   path("tasks/<int:pk>/", views.TaskDetailView.as_view(), name="task-detail"),
   path("tasks/create", views.TaskCreateView.as_view(), name="task_create")
]
