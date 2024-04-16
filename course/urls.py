from django.urls import path
from .views import CourseListView, TeacherListView
urlpatterns = [
    path('course/', CourseListView.as_view(), name='course'),
    path('teachers/', TeacherListView.as_view(), name='teacher')
]