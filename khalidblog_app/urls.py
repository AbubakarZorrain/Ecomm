from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import re_path

urlpatterns = [

path('',views.index, name="index"),
path('full_detail/<int:id>/',views.post_detail),
path('full_detail/<int:id>/<int:pid>/',views.reply),

]