from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Complaint

# Create your views here.


class ComplaintCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Complaint
    fields = ["title", "description"]
    success_url = reverse_lazy("complaints_list")
    template_name = "complaints_form.html"

    def test_func(self):
        return not self.request.user.is_superuser

    def form_valid(self, form):
        form.instance.flat = self.request.user
        return super(ComplaintCreateView, self).form_valid(form)


class ComplaintListView(LoginRequiredMixin, ListView):
    model = Complaint
    template_name = "complaints_list.html"
    paginate_by = 4

    def get_queryset(self):
        return Complaint.objects.filter(flat=self.request.user)
