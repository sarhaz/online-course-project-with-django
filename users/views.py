from django.shortcuts import render
from django.views import View
from blog.models import Blog
from course.models import Course, Speciality, Teacher


class DashboardView(View):
    def get(self, request):
        specialities = Speciality.objects.all()
        courses = Course.objects.all()
        teachers = Teacher.objects.all()
        blogs = Blog.objects.all()
        context = {
            'specialities': specialities,
            'courses': courses,
            'teachers': teachers,
            'blogs': blogs
        }
        return render(request, 'index.html', context)

