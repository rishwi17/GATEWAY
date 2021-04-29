from django.shortcuts import render
from .models import Contact
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


class ContactCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Contact
    template_name = "contacts_form.html"
    success_url = reverse_lazy("contacts_list")
    fields = "__all__"

    def test_func(self):
        return self.request.user.is_superuser


class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = "contacts_list.html"
