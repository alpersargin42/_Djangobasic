from django.contrib import admin
from courses.models import *

# Register your models here.
# admin.site.register(Course)
# admin.site.register(Category)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","slug","category",)
    list_filter = ("isActive","category",)
    prepopulated_fields = {"slug":("title",),}
    list_editable = ("isActive",)
    search_fields=("title","description",)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug","course_count",)
    prepopulated_fields = {"slug":("name",),}
    
    def course_count(self,obj):
        return obj.course_set.count()

admin.site.register(Course,CourseAdmin)
admin.site.register(Category,CategoryAdmin)