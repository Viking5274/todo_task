from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import TaskView, TaskDetailView, CommentList, CommentDetail, StatusView, StatusDetailView

app_name = "tasks"

urlpatterns = [
    path("tasks/", TaskView.as_view()),
    path("tasks/<int:pk>/", TaskDetailView.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('status/', StatusView.as_view()),
    path('status/<int:pk>/', StatusDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
