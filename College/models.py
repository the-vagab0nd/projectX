from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Batch(models.Model):
    code = models.CharField(max_length=100)


class UserRole(models.Model):
    role = models.CharField(max_length=20, choices=(('s','student'), ('f','faculty')))
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True)
    enrol = models.CharField(max_length=20)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)


class Course(models.Model):
    code = models.CharField(max_length=100)
    batch = models.ManyToManyField(Batch, through='CourseBatch')


class CourseBatch(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)


class attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
