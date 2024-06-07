from django.contrib import admin

from .models import Subject, Teacher, TeacherSubject, Class, Student


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    list_display_links = ['first_name', 'last_name']
    

@admin.register(TeacherSubject)
class TeacherSubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher', 'subject']
    list_display_links = ['teacher', 'subject']
    
    
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'class_field']
    list_display_links = ['first_name', 'last_name']
