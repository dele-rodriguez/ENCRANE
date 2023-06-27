from django.db import models
import Faculties.models as Faculty
from django.contrib.auth.models import User
from tinymce.models import *
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty.Faculties, on_delete = models.CASCADE, default = "")
    dept = models.ForeignKey(Faculty.Dept, on_delete=models.CASCADE, default="")
    level = models.CharField(max_length= 100, 
        choices=[('100', '100'), ('200', '200'), ('300', '300'), ('400', '400'), ('500', '500')])
    profile_pic = models.ImageField(upload_to="profile_picture", default = "")
    total_exams_taken = models.PositiveIntegerField(default = 0)
    total_marks = models.PositiveIntegerField(default = 0)
    time_spent = models.PositiveIntegerField(default = 0)
    posts = models.PositiveIntegerField(default = 0)
    comments = models.PositiveIntegerField(default = 0)

    def get_average_time(self):
        if self.total_exams_taken == 0:
            return 0
        self.time_spent = int(self.time_spent / self.total_exams_taken)
        hours = int(self.time_spent // 3600)
        minutes = int((self.time_spent % 3600) // 60)
        seconds = int((self.time_spent % 3600) % 3600)

        time_format = f"{hours:02d} : {minutes:02d} : {seconds:02d}"

        return time_format
    
    def get_average_mark(self):        
        if self.total_exams_taken == 0:
            return 0
        average_mark = self.total_marks / self.total_exams_taken
        return average_mark

    def __str__(self):
        return self.user.username 

