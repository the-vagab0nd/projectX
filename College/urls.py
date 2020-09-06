from django.contrib import admin
from django.urls import path, include
from .views import home_view, add_lecture_view, course_batch_view


urlpatterns = [
    path('', home_view),
    path('<course>/batch>/', course_batch_view),
    path('addLecture', add_lecture_view, name = "addLecture"),
]
