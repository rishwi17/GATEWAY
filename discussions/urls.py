from django.urls import path
from .views import DiscussionCreateView, DiscussionListView, discussions_detail


urlpatterns = [
    path("create", DiscussionCreateView.as_view(), name="discussions_create"),
    path("list", DiscussionListView.as_view(), name="discussions_list"),
    path("detail/<int:pk>", discussions_detail, name="discussions_detail"),
]