from sys import path_hooks
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about' ),
    path('contact/', views.contact, name='contact'),
]