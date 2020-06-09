from django.db import models


# Create your models here.

class Student(models.Model):
    Student_ID = models.IntegerField(unique=True, primary_key=True)
    Student_Year = models.CharField(max_length=100, null=True)


    def __str__(self):
        return str(self.Student_ID)

class Course(models.Model):
    Course_ID = models.CharField(unique=True, max_length=8, primary_key=True)
    Course_Name = models.CharField(max_length=100, null=True)


    def __str__(self):
        return str(self.Course_ID + ': ' + self.Course_Name)

class Grade(models.Model):
    Letter_Grade = models.CharField(unique=True, max_length=15, primary_key=True)
    Numerical_Weightage = models.FloatField()

    def __str__(self):
        return (self.Letter_Grade)

class Transcript(models.Model):
    Student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True, blank=True)
    Course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True, blank=True)
    Transcript_Grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return (str(self.Student) + ' : ' + str(self.Course) + ' : '+ str(self.Transcript_Grade))

class Prerequisite(models.Model):
    Desired_Course = models.ForeignKey('Course', on_delete=models.SET_NULL, related_name='main',
    null=True, blank=True)
    Course_Prerequisite = models.ForeignKey('Course', on_delete=models.SET_NULL, related_name='PreReq',
    null=True, blank=True)

    def __str__(self):
        return (str(self.Desired_Course) + ' : ' + str(self.Course_Prerequisite))
