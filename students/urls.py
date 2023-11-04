from django.urls import path
from . import views

app_name = "students"
urlpatterns = [
    path('' , views.students, name='student'),
    path('details/' , views.details, name='details'),
    path('courses/' , views.courses, name='courses'),
]
