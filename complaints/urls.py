from django.urls import path
from django.contrib.auth import logout, views
from .views import ComplaintCreateView, ComplaintListView

urlpatterns = [
    path("create", ComplaintCreateView.as_view(), name="complaints_create"),
    path("list", ComplaintListView.as_view(), name="complaints_list"),
]
