from rest_framework import serializers
from study.models import Lesson, LessonViewInfo
# from rest_framework.serializers import ModelSerializer


class MyLessonSerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    view_time = serializers.IntegerField()

    class Meta:
        model = Lesson
        fields = ('title', 'status', 'view_time')


# class MyLessonViewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lesson
#         fields = ('status', 'view_info')

class MyLessonByProductSerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    view_time = serializers.IntegerField()
    last_view_datetime = serializers.DateTimeField()

    class Meta:
        model = Lesson
        fields = ('title', 'status', 'view_time', 'last_view_datetime')
