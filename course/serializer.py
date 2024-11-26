from django import forms
from django.contrib.auth.models import User
from rest_framework import serializers   #导入序列化器
from .models import Course

class CourseForm(forms.ModelForm):    #配置表单
    class Meta:
        model = Course
        fields = ['name','price','introduction','teacher']

class UserSerializer(serializers.ModelSerializer):  #配置用户序列化器
    class Meta:
        model = User
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):  # 配置用户序列化器

    class Meta:
        model = Course
        # url 为默认字段名字，可以在setting.py 里面配置USER_URL_NAME来修改
        fields = ('name', 'price', 'introduction', 'teacher')
        depth = 1
