from django.contrib import admin
from .models import Board, Topic, Reply


class ReplyInlineModel(admin.StackedInline):
    model = Reply
    extra = 0


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'updated']
    inlines = [ReplyInlineModel]


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
