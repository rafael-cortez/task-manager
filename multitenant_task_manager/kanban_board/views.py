# views.py
from rest_framework import viewsets
from .models import Board, TaskList, Task
from .serializers import BoardSerializer, TaskListSerializer, TaskSerializer
from .permissions import IsTenantUser

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsTenantUser]


class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [IsTenantUser]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsTenantUser]