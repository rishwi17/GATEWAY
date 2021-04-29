from django.contrib import admin
from django.urls import path
from .views import ContactCreateView, ContactListView


urlpatterns = [
    path("create", ContactCreateView.as_view(), name="contacts_create"),
    path("list", ContactListView.as_view(), name="contacts_list"),
]
