from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [

    path('student/', StudentAPI.as_view()),

    path('', home),
    path('createStudent/', createStudent),
    path('updateStudent/<id>/', updateStudent),
    path('deleteStudent/<id>/', deleteStudent),
    path('getBook/', getBook),
    path('register/', RegisterUser.as_view()),

    path('genericStudent/', StudentGeneric.as_view()),
    path('genericStudent/<id>/', StudentGeneric1.as_view()),
]