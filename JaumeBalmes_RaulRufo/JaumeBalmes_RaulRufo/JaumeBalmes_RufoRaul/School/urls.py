from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alumnos/', views.alumnos, name='alum'),
    path('alumnos/alumno/<str:pk>/', views.alumno, name='alumno'),
    path('profesores/', views.profesores, name='prof'),
    path('profesores/profesor/<str:pk>/', views.profesor, name='profesor'),
]