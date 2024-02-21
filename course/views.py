from django.shortcuts import render
from course import models,serializer
from rest_framework import generics
from django.db.models import Count

class CourseListApiview(generics.ListAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializer.CourseSerializer


class UserStaticListApiview(generics.ListAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializer.UserInfoSerializer

    def get_queryset(self):
        user = self.kwargs.get('user')
        queryset = models.Lesson.objects.filter(lessonuserwatched__user=user)
        return queryset


class LessonStaticListApiView(generics.ListAPIView):
    serializer_class = serializer.LessonSerializer
    queryset = models.LessonUserWatched.objects.all()

    # def get_queryset(self):
    #     query = models.LessonUserWatched.objects.annotate(number = Count())


