from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Student)
admin.site.register(models.Course)
admin.site.register(models.Grade)
admin.site.register(models.Transcript)
admin.site.register(models.Prerequisite)
admin.site.register(models.SignificantCourse)
