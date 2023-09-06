from django.contrib import admin
from .models import *
# Register your models here.

class HostedExamAdmin(admin.ModelAdmin):
    list_display = ("examiner","title", "time_st", "time_end", "duration")

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("exam", "examiner")

admin.site.register(HostedExam, HostedExamAdmin)
admin.site.register(Question, QuestionAdmin)

