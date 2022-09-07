from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    department = forms.CharField(max_length=100)
    year_of_admission = forms.CharField(max_length=100)
    year_of_graduation = forms.CharField(max_length=100)
    year_of_birth = forms.DateField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.help_text = None

    class Meta:
        model = User
        fields = [
            'username', 'email',
            'first_name', 'last_name',
            'password1', 'password2'
        ]


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['department', 'year_of_admission', 'year_of_graduation', 'year_of_birth']
