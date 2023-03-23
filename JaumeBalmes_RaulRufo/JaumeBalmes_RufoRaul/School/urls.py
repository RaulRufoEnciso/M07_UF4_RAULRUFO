from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alumnos/', views.alumnos, name='alum'),
    path('profesores/', views.profesores, name='prof'),
]