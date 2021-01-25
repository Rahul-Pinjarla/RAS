from django import forms
from .models import TempFace, Lecture
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from datetime import datetime
import re
import string


class Studentface(forms.ModelForm):
    class Meta:
        model = TempFace
        fields = ['face']


class Lecture(forms.ModelForm):
    class Meta:
        model = Lecture
        exclude = ('lecturer',)
        widgets = {
            'lecture_time' : DateTimePicker,
        }
