from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', views.post_list, name='post_list'),
]