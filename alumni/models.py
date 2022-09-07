from django.db import models
from django.conf import settings
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='events')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']
        get_latest_by = 'date'

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Job(models.Model):
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    INTERNSHIP = 'IT'
    JOB_TYPE = (
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (INTERNSHIP, 'Internship'),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    company = models.CharField(max_length=100)
    job_type = models.CharField(max_length=2, choices=JOB_TYPE)
    description = models.TextField()
    salary = models.CharField(max_length=25)
    years_of_experience = models.IntegerField()
    location = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Spotlight(models.Model):
    """Alumni spotlight"""
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='spotlights')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
