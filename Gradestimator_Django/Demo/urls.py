from django.conf.urls import url

from . import views

app_name='Demo'

urlpatterns = [
    url(r'^$', views.DemoIndex.as_view(), name="demo_index"),
    url(r'related_course', views.CourseRelated, name="demo_two"),
    url(r'dashboard', views.dashboard, name="dashboard"),
    url(r'UVAdemo', views.CoursePredict, name="UVAdemo"),
]
