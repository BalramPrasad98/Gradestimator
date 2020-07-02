from django.db import models
from UVACS_Tables.models import Course, Grade
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class SignificantCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    Original_Course = models.ForeignKey('UVACS_Tables.Course', on_delete=models.SET_NULL,
    default = "", null=True, blank=True, related_name='original')
    SigCourse = models.ForeignKey('UVACS_Tables.Course', on_delete=models.SET_NULL,
    default = "", null=True, blank=True, related_name='associated')
    Grade = models.ForeignKey('UVACS_Tables.Grade', on_delete=models.SET_NULL,
    default = "", null=True, blank=True)

    def __str__(self):
        return str(self.SigCourse)
