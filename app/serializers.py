from rest_framework import serializers

from .models import Subject, Teacher, TeacherSubject, Class, Student


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
        

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
        
        
class TeacherSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSubject
        fields = "__all__"
        
        
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"
        
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"