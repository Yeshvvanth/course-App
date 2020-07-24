from django import forms
from .models import courses


class CourseForm(forms.ModelForm):
    class Meta:
        model = courses
        fields = ('title','course_video','course_pdf')
