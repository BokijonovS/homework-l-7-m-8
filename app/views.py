from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Subject, Teacher, TeacherSubject, Class, Student
from .serializers import SubjectSerializer, TeacherSerializer, TeacherSubjectSerializer, ClassSerializer, StudentSerializer


class SubjectAPIView(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class TeacherAPIView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class TeacherSubjectAPIView(viewsets.ModelViewSet):
    queryset = TeacherSubject.objects.all()
    serializer_class = TeacherSubjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
class ClassAPIView(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
class StudentAPIView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
