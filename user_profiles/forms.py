from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Faculties.models import Faculties, Dept


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', "email", "password1", "password2")

    # def save(self, commit = True):
        # user = super().save(commit=False)

        # user_username = self.cleaned_data["username"]
        # user_email = self.cleaned_data["email"]
# 
        # if commit:
            # user.save()
        # return user
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("faculty", "dept", "level", "profile_pic")