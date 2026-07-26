from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album/<int:album_id>/', views.album_detail, name='album'),
    path('timeline/', views.timeline, name='timeline'),
    path('discover/', views.discover, name='discover'),
]