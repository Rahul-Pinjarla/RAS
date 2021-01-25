from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from olms.models import UserProfile
from .models import Lecture, Lecturer, TempFace
from .import forms
from datetime import datetime
from django.db import models
import base64
import time

# Create your views here.
def main(res):
    return redirect('home')


def userhome(res):
    print('*'*10, 'schedule')
    try:
        print(Lecturer.objects.get(user=res.user))
        return redirect('lecturer')
    except:
        return redirect('student')


def usertype(res):
    print('schedule')
    if not isinstance(res.user, User) or res.user.is_superuser:
        print('*'*60)
        return redirect('logout')
    try:
        Lecturer.objects.get(user=res.user)
        return 'lecturer'
    except:
        return 'student'


def mainp(res):
    if usertype(res):
        try:
            print('trying usertype of res')
            return redirect(usertype(res).url)
        except:
            try:
                if (res.user.profile.usertype == 'admin' and usertype(res) == 'lecturer') or  usertype(res) == 'student':
                    if res.user.profile.usertype == 'security':
                        return redirect('/olms/sec_home')
                    return render(res, 'main.html', {})
            except:
                try:
                    if usertype(res) == 'lecturer':
                        return redirect(usertype(res))
                except:
                    pass


def student(res):
    if usertype(res) != 'student':
        return redirect('home')
    try:
        classs = Lecture.objects.filter(classs=res.user.profile.classs, lecture_time__gt=datetime.now())[0]
        print(classs)
        res.session['class_pk'] = classs.pk
    except:
        classs = 'no class'
        res.session['class_pk'] = None
    return render(res, 'student.html', {'class': classs})


def lecturer(res):
    if not isinstance(res.user, User):
        print('isnotuser')
        return redirect('login')
    if not usertype(res) == 'lecturer':
        return redirect('home')
    form = forms.Lecture()
    if res.method == 'POST':
        form = forms.Lecture(res.POST)
        if form.is_valid():
            form.save()
        else:
            return render(res, 'lecture.html', {'form': form})
    return render(res, 'lecture.html', {'form': form})


def facecam(res):
    if usertype(res) != 'student':
        return redirect('home')
    if res.method == 'POST':
        if res.is_ajax():
            face = TempFace()
            imgstring = base64.b64decode(res.POST['face'].replace('data:image/png;base64,', ''))
            imgdata = imgstring
            filename = f'oams/face-detection/{res.user.profile.id}.png'  # I assume you have a way of picking unique filenames
            with open(filename, 'wb') as f:
                f.write(imgdata)
                face.face = f'oams/face-detection/{res.user.profile.id}.png'
                face.save()
                time.sleep(15)
                f.write('') 
        return redirect('home')
    return render(res, 'facecam.html', {'form': forms.Studentface()}) 