from django.db import models
from django.contrib.auth.models import User

class Information(models.Model):
    user = models.OneToOneField(User)
    role = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
