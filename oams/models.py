from django.db import models
from olms import models as olms_models
from django.contrib.auth.models import User
import json

# Create your models here.


class Lecturer(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    is_hod = models.BooleanField(default=False)
    subject = models.CharField(max_length=50)
    branch = models.CharField(choices=olms_models.UserProfile.branches, max_length=5)
    year = models.CharField(choices=olms_models.UserProfile.years, max_length=10, default=None , null=True)


class Semester(models.Model):
    start_date = models.DateField(default=None)
    created_by = models.OneToOneField(Lecturer, related_name='HOD', on_delete=models.CASCADE)
    branch = models.CharField(choices=olms_models.UserProfile.branches, max_length = 5)
    subjects = models.CharField(max_length = 1000)
    lecturers = models.CharField(max_length = 1000)

    def set_subjects(subs):
        self.subjects = json.dumps(subs)

    def get_subjects():
        return json.loads(self.subjects)



class Lecture(models.Model):
    lecture_time = models.DateTimeField(default=None)
    lecture_duration = models.DurationField(default=None)
    lecturer = models.ForeignKey(Lecturer, related_name='lecturer', on_delete=models.CASCADE)
    classs = models.CharField(max_length=3)

class Attendence(models.Model):
    student = models.ForeignKey(olms_models.UserProfile, related_name='student', on_delete=models.CASCADE)
    attended = models.BooleanField(default=False)
    lecture = models.ForeignKey(Lecture, related_name='lecture', on_delete=models.CASCADE, default=None)

class Director(models.Model):
    user = models.ForeignKey(User, related_name='director', on_delete=models.CASCADE)


class TempFace(models.Model):
    face = models.ImageField(default=None, null=True, upload_to='tempfaces/', blank=True)