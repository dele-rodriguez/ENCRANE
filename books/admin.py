from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Books)
class CommentTheoryAdmin(admin.ModelAdmin):
    list_display = ('username', 'book_title', 'date_added', 'file')
