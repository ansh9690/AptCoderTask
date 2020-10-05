from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from core.models import Courses
from core.forms import CourseForm, CourseEnrollForm


class HomeView(ListView):
    model = Courses
    template_name = 'core/index.html'


class CourseListView(ListView):
    model = Courses
    template_name = 'core/courses.html'


class CourseDetailView(DetailView):
    model = Courses
    template_name = 'core/course_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView,
                        self).get_context_data(**kwargs)
        context['enroll_form'] = CourseEnrollForm(
            initial={'course': self.object})
        return context


@login_required(login_url='accounts:login')
def course_list(request):
    courses = Courses.objects.prefetch_related('students')
    return render(request, 'core/course_list.html', {"courses": courses})


@login_required(login_url='accounts:login')
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    form = CourseForm()
    context = {
        'form': form
    }
    return render(request, 'core/add_course.html', context)


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super(StudentEnrollCourseView,
                     self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('core:course_detail',
                            args=[self.course.slug])


class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Courses
    template_name = 'core/enroll_courses.html'

    def get_queryset(self):
        qs = super(StudentCourseListView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])
