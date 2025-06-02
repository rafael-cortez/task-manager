from datetime import timezone

from django.db import models

from .task_list import TaskList

class Task(models.Model):
    list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']  # Default ordering for Cards within a List

    def __str__(self):
        return self.title

    def is_overdue(self):
        """Checks if the card is overdue."""
        if self.due_date:
            return self.due_date < timezone.now().date()
        return False