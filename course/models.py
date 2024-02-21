from django.db import models
from users.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Course(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ManyToManyField(Course)
    title = models.CharField(max_length=128)
    link_video = models.CharField(max_length=256)
    total_time = models.IntegerField(default=0)

    def __str__(self):
        return self.title
class LessonUserWatched(BaseModel):
    user = models.ManyToManyField(User)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    from_time = models.IntegerField(default=0,unique=True)
    to_time = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return f"{self.user} bought --> {self.lesson}"
    def time_watched(cls):
        return cls.to_time - cls.from_time

    def is_finished(self):
        return self.Lesson.total_time* 0.8 <= self.time_watched
