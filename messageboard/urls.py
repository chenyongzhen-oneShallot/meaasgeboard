#coding=utf-8
from django.contrib import admin
from django.urls import path
from messageboard import views
from django.conf.urls import include

urlpatterns = [
    path(r'index/', views.index,name='index'),
    path(r'create/',views.create,name='create'),
    path(r'save/',views.save,name='save'),
]
