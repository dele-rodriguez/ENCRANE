from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.



class HostedExam(models.Model):
    id = models.CharField(default="", primary_key=True, editable=False, max_length=100)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    time_st = models.DateTimeField()
    time_end = models.DateTimeField()
    duration = models.PositiveIntegerField()
    examiner = models.ForeignKey(User, on_delete = models.CASCADE, default = "")

    def __str__(self):
        return self.title

class Question(models.Model):
    exam = models.ForeignKey("HostedExam", on_delete = models.CASCADE)
    examiner = models.ForeignKey(User, default = "", on_delete = models.CASCADE)

    question = HTMLField()
    op1 = models.TextField()
    op2 = models.TextField()
    op3 = models.TextField()
    op4 = models.TextField()

    answer = models.CharField(
        choices=(
            ("a", "a"),
            ("b", "b"),
            ("c", "c"), 
            ("d", "d"),
        ), max_length=100
    )

    def __str__(self):
        return str(self.exam)

# class Results(models.Model):

#     name = models.ForeignKey(User, on_delete = models.CASCADE)
#     exam = models.ForeignKey("HostedExam", on_delete=models.CASCADE)
#     score = models.PositiveIntegerField(default = 0)

#     def __str__(self):
#         return str(self.name)