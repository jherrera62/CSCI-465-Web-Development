from django import forms
from django.core import validators
from django.contrib.auth.models import User

class ChessForm(forms.Form):
    dst =forms.CharField(min_length=2,max_length=2, strip=True)
    src =forms.CharField(min_length=2,max_length=2, strip=True)
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
