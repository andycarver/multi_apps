from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import User
from ..course_bot.models import Course
# Create your models here.
class UserAddCourse(models.Model):
    course_add = models.ForeignKey(Course)
    user_add = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
