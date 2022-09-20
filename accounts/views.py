from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, ProfileForm


class SignUpView(SuccessMessageMixin, CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_message = "Registration successful. Create your Alumni profile."

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('create_profile')


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


def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'user': user})


def settings(request):
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
