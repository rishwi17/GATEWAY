from django.db import models
from django.urls import reverse
# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, default='')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('events:event_detail', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    def __str__(self):
        return self.title
