from django import forms
from .models import Topic, Reply


class NewTopicForm(forms.ModelForm):
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Start a discussion'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['title', 'body']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
