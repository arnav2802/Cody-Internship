from django.shortcuts import render , redirect
from django.shortcuts import HttpResponse
from Courses.models import Course , Video , UserCourse , cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def mycart(request , slug):
    course = Course.objects.get(slug = slug)
    user = request.user
    if (request.user.is_authenticated is False):
        return redirect ('login')
    
    if (request.user.is_authenticated):
        try : 
            cart.objects.get(user = user , course = course)
            return redirect('home')
        except :
               Cart= cart(user = user , course = course)
               Cart.save()

               context = {
                    "Course" : course ,
                    "Cart" : Cart

                }
               return render(request , template_name="Courses/mycart.html" , context = context)


@login_required(login_url="login")
def mycart1(request):
    user = request.user


    carts = cart.objects.filter(user=user)  
    userCourse = UserCourse.objects.filter(user=user)

    try:

        matched_carts = carts.filter(course_id__in=userCourse.values_list('course_id', flat=True))

        if matched_carts.exists():
            matched_carts.delete()
            print("Deleted matched items from cart.")

    except:
        print("Error occurred")

    remaining_carts = cart.objects.filter(user=user)

    context = {
        "carts": remaining_carts, 
        "user": user
    }

    return render(request, template_name="Courses/mycart1.html", context=context)


@login_required(login_url="login")
def personal(request):
    user = request.user
    userCourse = UserCourse.objects.filter(user = user)
    context = {
        'user' : user,
        'userCourse' : userCourse,
        "Course" : Course
        
    }
    return render(request , template_name="Courses/personal.html" , context = context)


def coursePage(request, slug):
    course = Course.objects.get(slug = slug)
    serial_number = request.GET.get('lecture')
    action = request.GET.get('action')
    user = request.user
    if serial_number is None:
        serial_number = 1
    video = Video.objects.get(serial_number = serial_number , course = course )
    if((request.user.is_authenticated is False) and (video.is_preview is False)):
        return redirect('login')
    if action == 'buy':
        userCourse = UserCourse(user = user , course = course)
        userCourse.save()
        print("UserCourse")
        context = {
        'userCourse' : userCourse,
        'course' : course
        }
        return render(request , template_name="Courses/paymentsuccess.html" , context = context )

    if(video.is_preview is False):
        try:
            hehe = UserCourse.objects.get( user = user , course = course)
            if(hehe is not False): 
                   pass      
        except:
            return render(request , template_name="Courses/check_out.html", context ={
                      "Course" : course,
                      "user" : user
                     })
            
    print(video)
    context = {
      "Course" :  course ,
      "video" : video
     
   }
    
    return render(request , template_name="Courses/course_page.html", context=context)               