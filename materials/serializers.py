from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lesson_count.all().count()

    class Meta:
        model = Course
        fields = ('title', 'description', 'lesson_count')


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'