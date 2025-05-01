from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('form',views.form,name="form"),
    path('upload',views.upload,name="upload"),
    path('',views.index),
    path('index',views.index,name="index")


]
