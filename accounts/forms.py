from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.help_text = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Username already exists. Try another.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Email already exists. Try another.')
        return email


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['fullname', 'date_of_birth', 'phonenumber', 'gender', 'about',
                  'passport', 'department', 'faculty', 'location', 'nationality',
                  'year_of_admission', 'year_of_graduation', 'post_held', 'project_topic',
                  'memorable_moment']

        widgets = {
            'memorable_moment': forms.Textarea(attrs={'rows': 4}),
            'about': forms.Textarea(attrs={'rows': 4}),
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date', 
                    'onkeydown': 'return false',
                    'min': '1990-01-01',
                    'max': '2006-12-31'}),
        }
