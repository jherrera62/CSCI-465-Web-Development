from django import forms
from django.contrib.auth.models import User
from django.core import validators
from budget.models import Budget, BudgetCategory

Task_Choices=(('home','Home'),('school','School'),('work','Work'),('self improvement','Self Improvement'),('other','Other'))

class BudgetEntryForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'size':'80'}))
    category=forms.CharField(widget=forms.Select(choices=Task_Choices))
    projected = forms.IntegerField()
    #actual = forms.CharField(widget=forms.TextInput(attrs={'size':'80'}))
    actual = forms.IntegerField()
    class Meta():
        model=BudgetCategory
        fields=('description','category','projected', 'actual')
