from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import Task
from .permissions import IsOwner
from .serializer import TaskSerializer, UserSerializer


class TasksList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    success_url = "?format=api"
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TasksDetail(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    success_url = "?format=api"
    permission_classes = [permissions.IsAuthenticated, IsOwner]
