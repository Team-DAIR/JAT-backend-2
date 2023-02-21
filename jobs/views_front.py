from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Job


class JobListView(LoginRequiredMixin, ListView):
    template_name = "jobs/job_list.html"
    model = Job
    context_object_name = "jobs"


class JobDetailView(LoginRequiredMixin, DetailView):
    template_name = "jobs/job_detail.html"
    model = Job
    context_object_name = "job"

class JobUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "jobs/job_update.html"
    model = Job
    fields = "__all__"
    context_object_name = "job"


class JobCreateView(LoginRequiredMixin, CreateView):
    template_name = "jobs/job_create.html"
    model = Job
    fields = "__all__" # "__all__" for all of them
    context_object_name = "job"


class JobDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "jobs/job_delete.html"
    model = Job
    success_url = reverse_lazy("job_list")
    context_object_name = "job"
