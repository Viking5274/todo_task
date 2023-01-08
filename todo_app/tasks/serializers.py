from rest_framework import serializers
from .models import (
    Task,
    Picture,
    Comment,
)


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    images = PictureSerializer(many=True)
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Task
        fields = "__all__"


class TaskDetailSerializer(serializers.ModelSerializer):
    images = PictureSerializer(many=True)
    author = serializers.ReadOnlyField(source="author.username")
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Task
        fields = "__all__"


class ChangeStatusSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    title = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = ["status", "author", "title", "id"]


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'task']
