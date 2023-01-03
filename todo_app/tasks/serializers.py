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
    # images = PictureSerializer(many=True)

    class Meta:
        model = Task
        fields = "__all__"
