from django.urls import path
from core.views import HomeView, course_list, CourseDetailView, add_course, CourseListView, StudentDetailView, TeacherDetailView, StudentEnrollCourseView, StudentCourseListView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('add/course/', add_course, name='add_course'),
    path('<slug:slug>/details/', CourseDetailView.as_view(), name='course_detail'),
    path('list/', course_list, name='course_list'),
    path('courses/list/', CourseListView.as_view(), name='courses'),
    path('enroll-course/', StudentEnrollCourseView.as_view(),
         name='student_enroll_course'),
    path('enroll/courses/', StudentCourseListView.as_view(),
         name='student_enroll_courses'),
    path('<slug:slug>/student/details/',
         StudentDetailView.as_view(), name='student_detail'),
    path('<slug:slug>/teacher/details/',
         TeacherDetailView.as_view(), name='teacher_detail'),

]
