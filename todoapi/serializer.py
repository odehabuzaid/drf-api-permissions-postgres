from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user")
    
    class Meta:
        model = Task
        fields = ("user", "task", "label", "created_at", "status")
        labels = {"status": "complete"}


class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = User
        fields = ["id", "username", "tasks", "owner"]
