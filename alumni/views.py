import datetime

from django.shortcuts import render, get_object_or_404

from .models import Event, Job


def home(request):

    return render(request, 'home.html', {})


def events(request):
    now = datetime.datetime.now()
    events = Event.objects.filter(date__gte=now)
    return render(request, 'events.html', {'events': events})


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'event_detail.html', {'event': event})


def job_list(request):
    jobs = Job.objects.all()

    return render(
        request, 'jobs.html', {'jobs': jobs})


def job_detail(request, id):
    job = get_object_or_404(Job, id=id)

    return render(
        request, 'job_detail.html', {'job': job,})


def forum(request):

    return render(request, 'forum.html', {})
