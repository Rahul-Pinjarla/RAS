from django.urls import path, include
from . import views
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
import django

urlpatterns = [
    path('', views.main, name='main'),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
    path('student', views.student, name='student'),
    path('home', views.userhome, name='home'), 
    path('lecturer', views.lecturer, name='lecturer'),
    path('facecam', views.facecam, name='facecam'),

] + static(settings.STATIC_URL, doucument_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)