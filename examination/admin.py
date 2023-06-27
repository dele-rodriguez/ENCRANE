from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Objectives)
admin.site.register(Theory)

@admin.register(CommentTheory)
class CommentTheoryAdmin(admin.ModelAdmin):
    list_display = ('username', 'date', 'question', 'content')

@admin.register(CommentObjective)
class CommentObjectiveAdmin(admin.ModelAdmin):
    list_display = ('username', 'date', 'question', 'content')