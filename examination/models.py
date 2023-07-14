from django.db import models
import Faculties.models as Faculty
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from user_profiles.models import UserProfile
import uuid
from datetime import datetime
# Create your models here.


# Exam and Study Mode - Objective and Theory Questions set up
class Objectives(models.Model):
    id = models.CharField(max_length = 1000000000000, default =uuid.uuid4, primary_key=True, editable = False)
    question = HTMLField()
    op1 = HTMLField()
    op2 = HTMLField()
    op3 = HTMLField()
    op4 = HTMLField()
    course = models.ForeignKey(Faculty.Courses, on_delete = models.CASCADE)
    correct_option = models.CharField(max_length=1000000, choices = (('a', 'a'), 
                                                                                 ('b', 'b'), 
                                                                                 ('c', 'c'), 
                                                                                 ('d', 'd')))
    explanation = HTMLField()

    def __str__(self):
        return str(self.course)

class Theory(models.Model):
    id = models.CharField(max_length = 1000000000000, default = uuid.uuid4, primary_key=True, editable = False)
    question  = HTMLField()
    ans = HTMLField()

    explanation = HTMLField()

    course = models.ForeignKey(Faculty.Courses, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.id)


# Comment Section

class CommentTheory(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null = True, blank = True)
    date = models.DateTimeField(max_length=100, default=datetime.now, blank=True)
    question = models.ForeignKey("Theory", on_delete=models.CASCADE, related_name ="Theory_Questions")
    content = HTMLField()

    class Meta:
        ordering = ['date']

    def __str__(self):

        return self.username.username

class CommentObjective(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null = True, blank = True)
    date = models.DateTimeField(max_length=100, default=datetime.now, blank=True)
    question = models.ForeignKey("Objectives", on_delete=models.CASCADE, related_name ="Objectives_Questions")
    content = HTMLField()

    class Meta:
        ordering = ['date']

    def __str__(self):

        return self.username.username

class StudentsTrials(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Faculty.Courses, on_delete=models.CASCADE)
    score = models.PositiveBigIntegerField()
    date = models.DateTimeField(default = datetime.now())

    def __str__(self):
        return self.username.username