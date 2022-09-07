from django.urls import path

from . import views

urlpatterns = [
    path('forum/', views.forum, name='forum'),
    path('jobs/', views.job_list, name='jobs'),
    path('job/<int:id>/', views.job_detail, name='job_detail'),
    path('events/', views.events, name='events'),
    path('event/<slug:slug>/', views.event_detail, name='event_detail'),
    path('', views.home, name='home'),
    
]
