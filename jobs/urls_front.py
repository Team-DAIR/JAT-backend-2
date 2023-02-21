from django.urls import path
from .views_front import (
    JobCreateView,
    JobDeleteView,
    JobDetailView,
    JobListView,
    JobUpdateView,
)

urlpatterns = [
    path("", JobListView.as_view(), name="job_list"),
    path("<int:pk>/", JobDetailView.as_view(), name="job_detail"),
    path("create/", JobCreateView.as_view(), name="job_create"),
    path("<int:pk>/update/", JobUpdateView.as_view(), name="job_update"),
    path("<int:pk>/delete/", JobDeleteView.as_view(), name="job_delete"),
]
