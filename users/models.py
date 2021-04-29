from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms


class Resident(AbstractUser):

    flatNo = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["flatNo"]

    def __str__(self):
        return self.username


class Vehicle(models.Model):
    name = models.CharField(max_length=30, null=False)
    number = models.CharField(max_length=10)
    owner = models.ForeignKey(
        Resident, on_delete=models.CASCADE, related_name="vehicles"
    )

    def __str__(self):
        return self.name


class Visitor(models.Model):
    name = models.CharField(max_length=30, null=False)
    purpose = models.TextField()
    number = models.CharField(max_length=12, null=False)
    flat = models.ForeignKey(
        Resident, on_delete=models.CASCADE, related_name='visitors')
    entryTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
