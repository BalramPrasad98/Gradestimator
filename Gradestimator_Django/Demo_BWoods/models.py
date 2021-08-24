from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

# Model for students
class Student(models.Model):
    Student_ID = models.IntegerField(unique=True, primary_key=True)
    Student_Year = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.Student_ID)

# Model for each of the courses that a student can take
class Course(models.Model):
    Course_ID = models.CharField(unique=True, max_length=8, primary_key=True)
    Course_Name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.Course_ID + ': ' + self.Course_Name)

# Model for each of the Grades that a student can have
class Grade(models.Model):
    Letter_Grade = models.CharField(unique=True, max_length=15, primary_key=True)
    Numerical_Weightage = models.FloatField()

    def __str__(self):
        return (self.Letter_Grade)

# Model for all of the grades that students get for each of their courses
class Transcript(models.Model):
    Student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True, blank=True)
    Course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True, blank=True)
    Transcript_Grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return (str(self.Student) + ' : ' + str(self.Course) + ' : '+ str(self.Transcript_Grade))

# Model with the courses that are related to each other - for this demo it is only
# the prerequisites
class Prerequisite(models.Model):
    Desired_Course = models.ForeignKey('Course', on_delete=models.SET_NULL, related_name='main',
    null=True, blank=True)
    Course_Prerequisite = models.ForeignKey('Course', on_delete=models.SET_NULL, related_name='PreReq',
    null=True, blank=True)

    def __str__(self):
        return (str(self.Desired_Course) + ' : ' + str(self.Course_Prerequisite))

# Temporary table for each user based on the courses that they selected
class SignificantCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
    related_name='userBWoods')
    Original_Course = models.ForeignKey('Course', on_delete=models.SET_NULL,
    default = "", null=True, blank=True, related_name='firstBWoods')
    SigCourse = models.ForeignKey('Course', on_delete=models.SET_NULL,
    default = "", null=True, blank=True, related_name='relatedBWoods')
    Grade = models.ForeignKey('Grade', on_delete=models.SET_NULL,
    default = "", null=True, blank=True)

    def __str__(self):
        return str(self.SigCourse)
