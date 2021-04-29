from django.db import models
from CommunityManagement import settings

# Create your models here.


class Discussion(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.title


class Reply(models.Model):
    body = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        Discussion, on_delete=models.CASCADE, related_name="replies"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return str(self.created_by) + "'s Reply"
