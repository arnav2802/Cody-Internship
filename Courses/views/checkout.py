from django.shortcuts import render , redirect
from django.shortcuts import HttpResponse
from Courses.models import Course , Video , Payment , UserCourse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt  



@login_required(login_url='/login')
def checkout(request , slug):
    user = request.user
    course = Course.objects.get(slug = slug)
    action = request.GET.get('action')
    order = None
    
    if action == 'create_payment':
        print("Creating Order")
        order = "Order Created"


    if action == 'buy':
        userCourse = UserCourse(user = user , course = course)
        userCourse.save()
        print("UserCourse")
        context = {
        'course' : course ,
        'userCourse' : userCourse
        }
        
        
        return render(request , template_name="Courses/paymentsuccess.html" , context = context )
        
        



    context = {
      "Course" : course ,
      "order" : order
   }


    return render(request , template_name="Courses/check_out.html", context=context)
               

