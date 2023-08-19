from django.contrib import admin
from.models import Course,Day,syllabus,Coursesyllabus

# Register your models here.
admin.site.register(Course)
admin.site.register(Day)
admin.site.register(syllabus)
admin.site.register(Coursesyllabus)
