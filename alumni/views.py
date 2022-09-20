import datetime

from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from accounts.models import Profile
from .models import Event, Job


def mk_paginator(request, items, num_items):
    """Create and return a paginator."""
    paginator = Paginator(items, num_items)
    page = request.GET.get('page', 1)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, return the first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range, return the last page of results.
        items = paginator.page(paginator.num_pages)
    return items


def home(request):

    return render(request, 'home.html', {})


def events(request):
    now = datetime.datetime.now()
    events = Event.objects.filter(date__gte=now)
    events = mk_paginator(request, events, 9)
    return render(request, 'events.html', {'events': events})


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'event_detail.html', {'event': event})


def job_list(request):
    jobs = Job.objects.all()
    jobs = mk_paginator(request, jobs, 9)
    return render(
        request, 'jobs.html', {'jobs': jobs})


def job_detail(request, id):
    job = get_object_or_404(Job, id=id)

    return render(
        request, 'job_detail.html', {'job': job,})


def forum(request):

    return render(request, 'forum.html', {})


def members(request):
    members = Profile.objects.all()
    members = mk_paginator(request, members, 9)
    return render(request, 'members.html', {'members': members})
