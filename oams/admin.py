from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Lecturer)
admin.site.register(models.Semester)
admin.site.register(models.Attendence)
admin.site.register(models.Lecture)
admin.site.register(models.Director)
admin.site.register(models.TempFace)