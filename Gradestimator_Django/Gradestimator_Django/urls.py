"""Gradestimator_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name='index'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    url(r"register/$", views.Register.as_view(), name="register"),
    url(r'^mission/$', views.MissionView.as_view(), name='mission'),
    url(r'^ourteam/$', views.OurTeam.as_view(), name='ourteam'),
    url(r'^edit/$', views.EditProfile, name='edit_profile'),
    url(r"^demo/", include("Demo.urls", namespace="demo")),

]
