from django.urls import path
from . import views

urlpatterns = [
     path('board/<slug:slug>/', views.board, name='board'),
     path('board/<int:pk>/newtopic/',
          views.new_topic, name='new_topic'),
     path('board/<int:pk>/topics/<int:topic_pk>/',
          views.topic, name='topic'),
     path('board/<int:pk>/topics/<int:topic_pk>/reply/',
          views.reply_topic, name='reply_topic'),
#     path('boards/<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/',
#          views.edit_post, name='edit_post'),    
     path('', views.forum, name='forum'),
]
