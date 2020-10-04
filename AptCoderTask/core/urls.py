from django.urls import path
from core.views import index, course_list, CourseDetailView, add_course, courses, StudentEnrollCourseView, StudentCourseListView

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('add/course/', add_course, name='add_course'),
    path('detail/<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('list/', course_list, name='course_list'),
    path('courses/list/', courses, name='courses'),
    path('enroll-course/', StudentEnrollCourseView.as_view(),
         name='student_enroll_course'),
    path('enroll/courses/', StudentCourseListView.as_view(),
         name='student_enroll_courses'),
]
