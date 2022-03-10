from django.conf import settings
from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.index),
    re_path(r'(\d+)/(\d+)', views.detail),
    path('upfile/',views.upfile),
    path('savefile/',views.savefile),
    #path('students/',views.students),
    re_path(r'studentPage/(\d+)',views.studentPage),
    path('ajaxstudent/',views.ajaxstudent),
    path('studentinfo/',views.studentinfo),
    path('edit/',views.edit),
    path('celery/',views.celery),

]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
