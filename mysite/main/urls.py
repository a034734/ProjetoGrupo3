from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("home/", views.home, name='home'),
    path("find/", views.find, name='find'),
    path("play/", views.play, name='play'),

]
