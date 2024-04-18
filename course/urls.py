from django.urls import path
from .views import CourseListView, TeacherListView, CourseDetailView, CourseUpdateView, CourseDeleteView, AddCourseView
urlpatterns = [
    path('course/', CourseListView.as_view(), name='course'),
    path('teachers/', TeacherListView.as_view(), name='teacher'),
    path('detail/<int:id>', CourseDetailView.as_view(), name='course-detail'),
    path('course/update/<int:id>', CourseUpdateView.as_view(), name='course-update'),
    path('course/delete/<int:id>', CourseDeleteView.as_view(), name='course-delete'),
    path('course/add/', AddCourseView.as_view(), name='add-new-course')
]