from django.contrib import admin
from .models import Teacher, Subject, Kafedra, Student, Group,  Faculted

# admin.site.register(Teacher)
@admin.register(Teacher)
class TaecherAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')

@admin.register(Kafedra)
class KafedraAdmin(admin.ModelAdmin):
    list_display = ('name','subject')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'kafedra')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'student')

@admin.register(Faculted)
class  FacultedAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')

