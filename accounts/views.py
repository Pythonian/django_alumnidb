from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, ProfileForm
from .models import Profile


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, 'Registration successful. Create your Alumni profile.')
            return redirect('create_profile')
        else:
            messages.warning(
                request, 'An error occured. Please check below.')
    else:
        form = SignUpForm()

    return render(request,
                  'registration/register.html',
                  {'form': form})


@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(
                request, 'Your alumni profile was successully created.')
            return redirect('profile', profile.user.username)
        else:
            messages.warning(
                request, 'Error creating your profile. Please check below.')
    else:
        form = ProfileForm()

    return render(request,
                  'profile_form.html',
                  {'form': form, 'create': True})


@login_required
def profile(request, username):
    try:
        Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        messages.warning(request, 'Please create an Alumni profile.')
        return redirect('create_profile')
    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'user': user})


@login_required
def settings(request):
    try:
        Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        messages.warning(request, 'Please create an Alumni profile.')
        return redirect('create_profile')
    if request.method == 'POST':
        form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account was successully updated.')
            return redirect('profile', request.user.username)
        else:
            messages.warning(
                request, 'There was an error while updating your account.')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'profile_form.html', {
        'form': form,
    })
