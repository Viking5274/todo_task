from rest_framework import generics

from .serializers import TaskSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Task
from .permissions import IsAuthorOrReadOnly


class TaskView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthorOrReadOnly | IsAdminUser]
