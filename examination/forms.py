from django import forms
from django.contrib.auth.models import User
from django.contrib .auth.forms import UserCreationForm
from examination.models import  *
from tinymce.widgets import TinyMCE

class CommentFormTheory(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(
        attrs={
        'rows': '4',
        'placeholder': 'Contribute...'
        }
    ))
    class Meta:
        model = CommentTheory
        fields = ('content',)


class CommentFormObjective(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={
        'rows': '4',
        'placeholder': 'Contribute...'
        }
    ))
    class Meta:
        model = CommentObjective
        fields = ('comment',)


