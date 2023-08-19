from django.db import models

class Course(models.Model):
    Course=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.Course
        class Meta:
            verbose_name_plural="Course"
class Day(models.Model):
    day=models.IntegerField(verbose_name="Days")
    is_active=models.BooleanField(default=True)
    

class syllabus(models.Model):
    syllabus=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.syllabus
        class Meta:
            verbose_name_plural="syllabus"
class Coursesyllabus(models.Model):
    course=models.OneToOneField(Course,on_delete=models.CASCADE)
    day=models.OneToOneField(Day,on_delete=models.CASCADE)
    syllabus=models.ManyToManyField(syllabus)
    percentage=models.CharField(max_length=200)
    class Meta:
        verbose_name_plural="Course syllabus"
        

