from django import forms
from django.core import validators
from django.contrib.auth.models import User
from core.models import UserProfile
class JoinForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'size':'30'}))
    class Meta():
        model=User
        fields=('first_name','last_name','username','email','password')
        help_texts={
            'username':None
        }
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
class UserProfileMF(forms.ModelForm):
    class Meta():
        model=UserProfile
        fields=('tasks_view_hide_completed',)
