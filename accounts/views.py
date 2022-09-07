from django.shortcuts import render


def register(request):

    return render(request, 'registration/register.html', {})


def profile(request):
    return render(request, 'profile.html', {'user': request.user})


def settings(request):
    return render(request, 'settings.html', {})
