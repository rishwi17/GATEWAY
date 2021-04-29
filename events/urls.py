from django.conf.urls import url
from . import views

app_name = 'events'
urlpatterns = [

    url('calendar', views.CalendarView.as_view(), name='calendar'),
    url(r'detail/(?P<pk>\d+)',
        views.EventDetailView.as_view(), name='event_detail'),
]
