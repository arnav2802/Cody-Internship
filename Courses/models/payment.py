from django.db import models
from Courses.models import Course
from Courses.models import UserCourse
from django.contrib.auth.models import User

class Payment(models.Model):
    order_id = models.CharField( max_length=50 , null =False)
    payment_id = models.CharField( max_length=50 )
    user = models.ForeignKey(User  , on_delete = models.CASCADE)
    Course = models.ForeignKey(Course ,  on_delete = models.CASCADE)
    user_course = models.ForeignKey(UserCourse , null = False , on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)