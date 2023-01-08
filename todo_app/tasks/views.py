from rest_framework import generics
from rest_framework.exceptions import ValidationError

from .serializers import TaskSerializer, ChangeStatusSerializer, TaskDetailSerializer, CommentSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Task, Comment, Status
from .permissions import IsAuthor, IsAssignee


class TaskView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = [IsAuthor | IsAdminUser | IsAssignee]


class StatusView(generics.ListAPIView):
    serializer_class = ChangeStatusSerializer
    queryset = Task.objects.all()


class StatusDetailView(generics.UpdateAPIView):
    serializer_class = ChangeStatusSerializer
    permission_classes = [IsAuthor | IsAdminUser | IsAssignee]
    queryset = Task.objects.all()

    def perform_update(self, serializer):
        if IsAssignee:
            if serializer.validated_data["status"] in Status.objects.filter(visibility=0):
                raise ValidationError("you cannot set this status")
        serializer.save()


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor | IsAuthenticatedOrReadOnly]
