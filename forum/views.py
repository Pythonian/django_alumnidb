from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from .forms import NewTopicForm, ReplyForm
from .models import Board, Topic, Reply


def mk_paginator(request, items, num_items):
    '''Create and return a paginator.'''
    paginator = Paginator(items, num_items)
    page = request.GET.get('page', 1)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        items = paginator.page(paginator.num_pages)
    return items


@login_required
def forum(request):
    boards = Board.objects.all()

    return render(request, 'forum.html', {'boards': boards})


@login_required
def board(request, slug):
    board = get_object_or_404(Board, slug=slug)
    # Return the count of replies for a given topic.
    topics = board.topics.order_by(
        '-created').annotate(replies_count=Count('replies'))
    topics = mk_paginator(request, topics, 20)
    popular_topics = board.topics.order_by('-views')[:3]

    # Create a session key for a user
    session_key = 'viewed_board_{}'.format(board.pk)
    if not request.session.get(session_key, False):
        board.views += 1
        board.save()
        request.session[session_key] = True

    return render(request, 'board.html', {'board': board, 'topics': topics, 'popular_topics': popular_topics})


@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.author = request.user
            topic.save()
            return redirect('topic', pk=pk, topic_pk=topic.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})


@login_required
def topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    replies = topic.replies.order_by('created')
    replies = mk_paginator(request, replies, 20)

    # Create a session key for a user
    session_key = 'viewed_topic_{}'.format(topic.pk)
    if not request.session.get(session_key, False):
        topic.views += 1
        topic.save()
        request.session[session_key] = True

    template = 'topic.html'
    context = {
        'topic': topic,
        'replies': replies,
    }

    return render(request, template, context)


@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.topic = topic
            reply.created_by = request.user
            reply.save()

            topic.updated = timezone.now()
            topic.save()

            topic_url = reverse('topic', kwargs={
                                'pk': pk, 'topic_pk': topic_pk})
            topic_reply_url = '{url}?page={page}#{id}'.format(
                url=topic_url,
                id=reply.pk,
                page=topic.get_page_count()
            )
            # Sends user to the last page
            return redirect(topic_reply_url)
    else:
        form = ReplyForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})
