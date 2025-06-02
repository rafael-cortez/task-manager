# urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'boards', views.BoardViewSet)
router.register(r'lists', views.TaskListViewSet)
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]