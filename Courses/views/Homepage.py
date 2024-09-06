from django.shortcuts import render
from Courses.models import Course , cart
from django.shortcuts import HttpResponse


def home(request  ):
    Courses = Course.objects.all()
    print(Courses)



    return render(request , template_name="Courses/home.html" ,
                 context={"Courses" : Courses} )