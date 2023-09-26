from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Faculties)
admin.site.register(Courses)
admin.site.register(Dept)
admin.site.register(Department_Courses)