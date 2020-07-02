from django import forms
from django.forms import ModelForm
from UVACS_Tables.models import Course, Grade
from Analytics.models import SignificantCourse
from django.forms import ModelChoiceField


class CourseForm(ModelForm):
    Course = ModelChoiceField(queryset=Course.objects.all().exclude(Course_ID='CS 1110'),
    initial=None, empty_label="Select a Course")

    class Meta:
         model = Course
         fields = ['Course']

class PreReqForm(forms.Form):

    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra')
        super(PreReqForm, self).__init__(*args, **kwargs)

        for i, question in enumerate(extra):
            self.fields['custom_%s' % i] = forms.ModelChoiceField(
            queryset=Grade.objects.all().exclude(Letter_Grade='No Grade'),
            label=question, empty_label="Select Grade")

    def extra_answers(self):
        for name, value in self.cleaned_data.items():

            if name.startswith('custom_'):
                yield (self.fields[name].label, value)
