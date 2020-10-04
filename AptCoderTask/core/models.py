from django.db import models
from django_extensions.db.fields import AutoSlugField
from accounts.models import User


class Courses(models.Model):
    owner = models.ForeignKey(User,
                              related_name='courses_created',
                              on_delete=models.CASCADE)
    course_name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    instructer = models.CharField(max_length=150, blank=True, null=True)
    students = models.ManyToManyField(User, related_name='courses_joined',
                                      blank=True)
    slug = AutoSlugField(('slug'), max_length=50,
                         unique=True, populate_from=('course_name',))

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        pass

    class Meta:
        ordering = ['-date']
