from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

STATUS_CHOICES = [
    ('applied', 'Applied'),
    ('pending', 'Pending'),
    ('rejected', 'Rejected')
]


class Job(models.Model):
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    company = models.TextField(blank=True)
    job_title = models.TextField(blank=True)
    date_applied = models.DateField()
    notes = models.TextField(blank=True)
    method_of_applications = models.TextField(blank=True)
    referrals = models.TextField(blank=True)
    first = models.BooleanField(default=False)
    second = models.BooleanField(default=False)
    third = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])
