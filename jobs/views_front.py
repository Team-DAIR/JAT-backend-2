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


class JobUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "jobs/job_update.html"
    model = Job
    fields = ["job_title", "notes"]


class JobCreateView(LoginRequiredMixin, CreateView):
    template_name = "jobs/job_create.html"
    model = Job
    fields = ["company","job_title","date_applied", "notes", "method_of_applications","referrals"] # "__all__" for all of them


"""company = models.TextField(blank=True)
    job_title = models.TextField(blank=True)
    date_applied = models.DateField()
    notes = models.TextField(blank=True)
    method_of_applications = models.TextField(blank=True)
    referrals = models.TextField(blank=True)"""

class JobDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "jobs/job_delete.html"
    model = Job
    success_url = reverse_lazy("job_list")
