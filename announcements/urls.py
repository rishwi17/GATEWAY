from django.contrib import admin
from django.urls import path
from django.contrib.auth import logout, views
from .views import AnnouncementCreateView, AnnouncementListView

urlpatterns = [
    path("create", AnnouncementCreateView.as_view(), name="announcements_create"),
    path("list", AnnouncementListView.as_view(), name="announcements_list"),
]
