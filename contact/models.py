from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=50)
    movil = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=50)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name

