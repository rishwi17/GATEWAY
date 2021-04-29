# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, views
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ValidationError
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView

from .forms import ResidentCreationForm, ResidentUpdateForm
from .models import Resident, Vehicle


def indexview(request):
    if request.user.is_authenticated:
        return redirect("announcements_list")
    else:
        return render(request, "index.html")


class Signup(SuccessMessageMixin, generic.CreateView):
    template_name = "signup.html"
    success_url = reverse_lazy("waiting")
    form_class = ResidentCreationForm


class Signin(views.LoginView):
    template_name = "signin.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("announcements_list")

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_verified:
                login(self.request, user)
                if self.request.GET.get("next"):
                    return HttpResponseRedirect(self.request.POST.get("next"))
                return HttpResponseRedirect(self.success_url)
            else:
                return HttpResponseRedirect('waiting')
        else:
            return self.form_invalid(form)


class ResidentListView(ListView):
    model = Resident
    template_name = "users_list.html"
    ordering = ["-flatNo"]

    def get_queryset(self):
        return Resident.objects.filter(is_superuser=False).filter(visible=True)


class VehicleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Vehicle
    fields = ['name', 'number']
    success_url = reverse_lazy('profile')
    template_name = 'vehicle_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(VehicleCreateView, self).form_valid(form)


class ResidentUpdateView(LoginRequiredMixin, UpdateView):
    model = Resident
    # form_class = ResidentUpdateForm
    template_name = 'resident_update.html'

    fields = ['username', 'email', 'visible']

    success_url = reverse_lazy("profile")


class ProfileView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'profile.html'

    def get_queryset(self):
        return Vehicle.objects.filter(owner=self.request.user)


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    success_url = reverse_lazy('profile')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
