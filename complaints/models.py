from django.db import models
from CommunityManagement import settings

# Create your models here.


class Complaint(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    flat = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="complaints", on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    solved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.title