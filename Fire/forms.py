from django import forms
from .models import Event,Comment
from django.contrib.auth.models import User

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=['event_creator','event_password','banner','event','venue','date','time','contacts','cash','description']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['user_name','opinions']

class LoginForm(forms.ModelForm):
    event_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Event
        fields=['event_creator','event_password']


