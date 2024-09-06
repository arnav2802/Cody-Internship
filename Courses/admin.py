from django.contrib import admin
from Courses.models import Course , Payment , UserCourse , Tag , Prerequisites , Learning, Video , cart


class TagAdmin(admin.TabularInline):
    model = Tag
class LearningAdmin(admin.TabularInline):
    model = Learning
class PrerequisitesAdmin(admin.TabularInline):
    model = Prerequisites
class VideoAdmin(admin.TabularInline):
    model = Video



class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin , LearningAdmin , PrerequisitesAdmin, VideoAdmin]
    list_display = ["name", 'get_price' , 'get_discount' , 'active']

    def get_discount(self , course):
        return f'{course.discount}%'
    def get_price(self , course):
        return f'{course.price}Rs'
    
    get_discount.short_description="Discount"

    get_price.short_desccription="Price"

admin.site.register(Course, CourseAdmin)
admin.site.register(Video)
admin.site.register(Payment)
admin.site.register(UserCourse)
admin.site.register(cart)

