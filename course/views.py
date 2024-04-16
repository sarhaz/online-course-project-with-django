from django.shortcuts import render
from django.views import View
from .models import Course, Teacher


class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        context = {
            "courses": courses
        }
        return render(request, 'course.html', context)


class TeacherListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        context = {
            "teacher": teachers
        }
        return render(request, 'teacher.html', context)
