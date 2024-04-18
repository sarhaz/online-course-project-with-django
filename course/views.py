from urllib import request

from django.shortcuts import render, redirect
from django.views import View
from .models import Course, Teacher


class CourseListView(View):
    def get(self, request):
        search = request.GET.get('search')
        if not search:
            courses = Course.objects.all()
            context = {
                "courses": courses,
                "search": search
            }
            return render(request, 'course.html', context)
        else:
            courses = Course.objects.filter(name__icontains=search)
            if courses:
                context = {
                    "courses": courses,
                    "search": search
                }
                return render(request, 'course.html', context)
            else:
                context = {
                    "courses": courses,
                    "search": search
                }
                return render(request, 'course.html', context)


class TeacherListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        context = {
            "teachers": teachers
        }
        return render(request, 'teacher.html', context)


class CourseDetailView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        return render(request, 'course_detail.html', {'course': course})


class CourseUpdateView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        return render(request, 'course_update.html', {'course': course})

    def post(self, request, id):
        new_name = request.POST.get('name')
        new_description = request.POST.get('description')
        new_price = request.POST.get('price')
        image = request.POST.get('image')

        course = Course.objects.get(id=id)
        course.name = new_name
        course.description = new_description
        course.price = new_price
        course.image = image
        course.save()

        return redirect('course')


class CourseDeleteView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return redirect('course')


class AddCourseView(View):
    def get(self, request):
        return render(request, 'add_course.html')

    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.POST.get('image')
        price_type = request.POST.get('price_type')

        course = Course(name=name, description=description, price=price, price_type=price_type, image=f"course/course/{image}")
        course.save()
        return redirect('course')


