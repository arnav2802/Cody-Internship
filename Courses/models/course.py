from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200, null = False)
    slug = models.CharField(max_length=50, null = True , unique= True)
    discription = models.CharField (max_length= 200, null= True)
    price = models.IntegerField(null=False, default= 0)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to="files/thumbnail")
    date = models.DateTimeField(auto_now_add=True) 
    length = models.IntegerField(null=False)

    def __str__(self):
       return self.name




class CourseProperty(models.Model):
    discription = models.CharField(max_length= 20 , null =False)
    course = models.ForeignKey(Course , null = False , on_delete = models.CASCADE)

    class Meta :
       abstract = True 




class Tag(CourseProperty):
    pass

class Prerequisites(CourseProperty):
   pass

class Learning(CourseProperty):
  pass

