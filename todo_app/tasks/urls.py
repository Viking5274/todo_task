from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TaskView, TaskDetailView

app_name = 'tasks'

# router = DefaultRouter()
# router.register("tasks", TaskView, "tasks")
# router.register("tasks/<int:pk>/", TaskDetailView, "tasks_detail")
# urlpatterns = [
#               ] + router.get_urls()

urlpatterns = [
    # code omitted for brevity
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
]
