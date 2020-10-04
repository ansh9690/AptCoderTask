from django import forms
from core.models import Courses


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['owner', 'course_name', 'description', 'instructer', ]


class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Courses.objects.all(),
                                    widget=forms.HiddenInput)