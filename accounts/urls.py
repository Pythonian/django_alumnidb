from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('create_profile/', views.create_profile, name='create_profile'),
    path('settings/', views.settings, name='settings'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('logout/',
         auth_views.LogoutView.as_view(), name='logout'),
    path('login/',
         auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('<str:username>/', views.profile, name='profile'),
]
