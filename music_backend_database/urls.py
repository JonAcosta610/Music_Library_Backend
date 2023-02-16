from django.urls import path
from . import views

urlpattern = [
    path('', views.music_list),
]