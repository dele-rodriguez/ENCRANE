from django.db import models
from datetime import datetime
# Create your models here.

class Books(models.Model):
    username = models.CharField(max_length=100)
    book_title = models.CharField(max_length=100)

    date_added = models.DateTimeField(default = datetime.now())
    file = models.FileField(upload_to="books")

    def __str__(self):
        return self.username