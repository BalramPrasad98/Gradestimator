from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

from . import models
from Profiles.models import Student, Course, Grade, Prerequisite, Transcript
from Analytics.models import SignificantCourse
from .forms import CourseForm, PreReqForm
from analytics import runanalytics
# Create your views here.

class DemoIndex(TemplateView):
    template_name = 'demo/main_index.html'

def CoursePredict(request):

    template_name = 'demo/demoUVA_index.html'

    if request.method == 'POST':
        form = CourseForm(request.POST or None)

        if form.is_valid():
            SignificantCourse.objects.filter(user=request.user).delete()
            prereqs_table = Prerequisite.objects.filter(
            Desired_Course=form.cleaned_data['Course']).values('Course_Prerequisite')
            for p in prereqs_table:
                c = Course.objects.get(Course_ID=p['Course_Prerequisite'])
                SignificantCourse.objects.create(user=request.user,
                Original_Course = form.cleaned_data['Course'],
                SigCourse = c, Grade = None)
        return HttpResponseRedirect(reverse('demo:demo_two'))

    else:
        form = CourseForm()

    context = {
        "course_selection":form,
    }

    return render(request, template_name, context)

def CourseRelated(request):

    template_name = 'demo/related_courses.html'

    extra_questions = list(SignificantCourse.objects.filter(user=request.user))
    form = PreReqForm(request.POST or None, extra=extra_questions)

    if request.method == 'POST' and 'run_analytics' in request.POST:
        if form.is_valid():
            for (question, answer) in form.extra_answers():
                question.Grade = answer
                question.save()

        return HttpResponseRedirect(reverse('demo:dashboard'))

    Course_list = list(SignificantCourse.objects.filter(user=request.user).values('Original_Course').distinct())

    context = {
        "form":form,
        "original_course": Course_list,
    }
    return render(request, template_name, context)

def dashboard(request):

    template_dashboard = 'demo/dashboard.html'

    my_courses = SignificantCourse.objects.filter(user=request.user)
    pc = runanalytics(my_courses)
    if(isinstance(pc,str)):
        failure_dashboard = 'demo/failure_dashboard.html'
        context = {"failure_message": pc}
        return render(request, failure_dashboard, context)

    pie_chart = pc[0].to_html(full_html=False, default_height=500, default_width=700)
    predicted_grade = pc[1]
    predicted_course = pc[2]
    total_course_num = pc[3]
    significant_course_num = pc[4]

    context = {
        "pie_chart": pie_chart,
        "predicted_grade": predicted_grade,
        "predicted_course": predicted_course,
        "total_students": total_course_num,
        "significant_students": significant_course_num,
    }
    return render(request, template_dashboard, context)
