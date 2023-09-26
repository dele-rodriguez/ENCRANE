from django.db import models
from tinymce.models import HTMLField
from datetime import datetime
from django.contrib.auth.models import *
from user_profiles.models import UserProfile
import uuid

# Create your models here.

class PostQuestion(models.Model):
    id = models.CharField(max_length = 1000000000000, default = uuid.uuid4, primary_key=True, editable = False)
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete = models.CASCADE, null = True, blank = True)
    date = models.DateTimeField(max_length=100, default = datetime.now)
    post = HTMLField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return str(self.id)
    
class Comment(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null = True, blank = True)
    date = models.DateTimeField(max_length=100, default = datetime.now, blank = True)
    question = models.ForeignKey("PostQuestion", on_delete = models.CASCADE, related_name="Questions")
    content = HTMLField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.username.username

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length =  100)
    review = models.CharField(max_length = 1000, default = "")

    def __str__(self):
        return self.email