from django.urls import path
from course import views

urlpatterns = [
    path("",views.CourseListApiview.as_view()),
    path("userlessons/", views.UserStaticListApiview.as_view())
]
