
from django.contrib import admin
from django.urls import path , include
from Courses.views import home , coursePage , SignupView , LoginView , signout , checkout , mycart, personal, mycart1
from django.conf.urls.static import static
from Cody.settings import MEDIA_ROOT , MEDIA_URL
from django.conf import settings

urlpatterns = [
    path('',home, name='home'),
    path('logout', signout , name='logout'),
    path('signup', SignupView.as_view() , name = 'signup' ),
    path('login', LoginView.as_view() , name = 'login' ),
    path('mycart/<str:slug>', mycart , name = 'mycart'),
    path('mycart1', mycart1 , name = 'mycart1'),
    path('personal', personal , name = 'personal'),
    path('course/<str:slug>', coursePage , name='coursepage'),
    path('check-out/<str:slug>', checkout , name='Checkpage')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)