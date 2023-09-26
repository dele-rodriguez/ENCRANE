from django.db import models

# Create your models here.

class Faculties(models.Model):
    faculty = models.CharField(max_length=100)

    
    class Meta:
        ordering = ['faculty']

    def __str__(self):
        return self.faculty
    
class Courses(models.Model):
    course = models.CharField(max_length=100)

    
    class Meta:
        ordering = ['course']

    def __str__(self):
        return self.course
    
class Dept(models.Model):
    dept = models.CharField(max_length=100, default = "")
    faculty = models.ForeignKey("Faculties", on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['dept']

    def __str__(self):
        return self.dept
    
class Department_Courses(models.Model):
    department = models.ForeignKey("Dept", on_delete = models.CASCADE)

    courses = models.ManyToManyField("Courses", related_name="my_courses")

    def __str__(self):
        return str(self.department)