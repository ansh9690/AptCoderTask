from django.urls import path
from accounts.views import login_view, SignUpView, StudentSignUpView, TeacherSignUpView, logout_view, teacher_profile, student_profile

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/student/',
         StudentSignUpView.as_view(), name='student_signup'),
    path('signup/teacher/',
         TeacherSignUpView.as_view(), name='teacher_signup'),
    path('logout/', logout_view, name='logout'),
    path('teacher/profile/', teacher_profile, name='teacher_profile'),
    path('student/profile/', student_profile, name='student_profile'),
]
