from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import VideoValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        validators = [VideoValidator(field='video_link')]
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(source='lesson_count', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_count', many=True, read_only=True)

    def get_lesson_count(self, course):
        return Lesson.objects.filter(course=course).count()
    class Meta:
        model = Course
        fields = ('lessons', 'title', 'description', 'lesson_count', 'image', 'owner')