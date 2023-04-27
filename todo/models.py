from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    done = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
