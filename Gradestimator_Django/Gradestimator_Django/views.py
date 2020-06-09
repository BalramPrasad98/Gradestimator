from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(TemplateView):
    template_name = 'index.html'

class MissionView(TemplateView):
    template_name = 'about/mission.html'

class OurTeam(TemplateView):
    template_name = 'about/ourteam.html'

# Used a Library for login page

class Register(CreateView):
    form_class = forms.Registration_Form
    success_url = reverse_lazy("login")
    template_name = "registration/registration.html"

def EditProfile(request):
    if request.method == 'POST':
        form = forms.EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            update = form.save()
            update.user = request.user
            update.save()
            return HttpResponseRedirect('/')
    else:
        form = forms.EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/update.html', args)
