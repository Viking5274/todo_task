from rest_framework import serializers
from .models import (
    Task,
    Picture,
)


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    images = PictureSerializer(many=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Task
        fields = "__all__"
