import math
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import Truncator


class Board(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def get_topics_count(self):
        return Topic.objects.filter(board=self).count()

    def get_replies_count(self):
        return Reply.objects.filter(topic__board=self).count()

    def get_absolute_url(self):
        return reverse('board', kwargs={'slug': self.slug})

    # def get_last_reply(self):
    #     return Reply.objects.filter(topic__board=self).order_by('-created').first()

    def get_last_topic(self):
        return Topic.objects.filter(board=self).order_by('-created').first()


class Topic(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=4000)
    board = models.ForeignKey(
        Board, related_name='topics', on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, related_name='topics', on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topic', kwargs={'pk': self.board.pk, 'topic_pk': self.pk})

    def get_page_count(self):
        count = self.replies.count()
        pages = count / 2
        return math.ceil(pages)

    def has_many_pages(self, count=None):
        if count is None:
            count = self.get_page_count()
        return count > 2

    def get_page_range(self):
        count = self.get_page_count()
        if self.has_many_pages(count):
            return range(1, 5)
        return range(1, count + 1)

    def get_last_ten_replies(self):
        return self.replies.order_by('-created')[:10]


class Reply(models.Model):
    body = models.TextField(max_length=4000)
    topic = models.ForeignKey(
        Topic, related_name='replies', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, related_name='replies', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User, null=True, related_name='+', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True)

    def __str__(self):
        truncated_body = Truncator(self.body)
        return truncated_body.chars(30)
