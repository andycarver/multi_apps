from __future__ import unicode_literals
from ..login_registration.models import User
from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user_add = models.ManyToManyField(User)
