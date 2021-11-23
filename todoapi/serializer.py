from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Task
        fields = ("task", "label", "created_at", "status", "user")
        labels = {"status": "complete"}


class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = User
        fields = ["id", "username", "tasks", "owner"]
