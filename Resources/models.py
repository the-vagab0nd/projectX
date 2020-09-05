from django.db import models
from College.models import Batch, Course
# Create your models here.


class Lecture(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Video(models.Model):
    embeded_code = models.CharField(max_length=100)
    lecture = models.CharField(max_length=100)
