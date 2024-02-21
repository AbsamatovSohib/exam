from rest_framework import serializers
from course import models

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ("title",)


class LessonSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField(source='course.title', read_only=True)
    class Meta:
        model = models.Lesson
        fields= ("title","link_video","total_time","course")


class LessonUserWatchedSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = models.LessonUserWatched
        fields = ("user","lesson","from_time","to_time","lesson","is_finished")


class UserInfoSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = models.LessonUserWatched
        fields = ("created_at","lesson")

