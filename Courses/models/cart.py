from django.db import models
from Courses.models import Course
from django.contrib.auth.models import User

class cart(models.Model):
    user = models.ForeignKey(User  , on_delete = models.CASCADE)
    course = models.ForeignKey(Course ,  on_delete = models.CASCADE)
    slug = models.CharField(max_length=50, null = True , unique= True)
    def __str__(self):
       return f'{self.user} - {self.course}'