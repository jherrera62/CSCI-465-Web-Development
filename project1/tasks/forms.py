from django import forms
from django.contrib.auth.models import User
from django.core import validators
from tasks.models import Task, TaskCategory

Task_Choices=(('home','Home'),('school','School'),('work','Work'),('self improvement','Self Improvement'),('other','Other'))

class TaskEntryForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'size':'80'}))
    category=forms.CharField(widget=forms.Select(choices=Task_Choices))
    class Meta():
        model=TaskCategory
        fields=('description','category')
