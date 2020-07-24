from django.urls import path
from . import views



urlpatterns = [
    
    # path('upload/',views.upload, name='upload'),
    path('courses/',views.course_list,name="course_list"),
     path('courses/upload',views.upload_courses,name="upload_course"),
     path('courses/<int:pk>/',views.delete_course,name="delete_course")
]

