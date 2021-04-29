from django.db import models
from users.models import Resident
from django.contrib.auth.models import User
from CommunityManagement import settings

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title