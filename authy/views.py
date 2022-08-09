from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from authy.models import Profile
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def SideNavInfo(request):
    user = request.user
    nav_profile = None

    if user.is_authenticated:
        nav_profile = Profile.objects.get(user=user)

    return {'nav_profile': nav_profile}


def UserProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    template = loader.get_template('profile.html')

    context = {
        'profile': profile,

    }

    return HttpResponse(template.render(context, request))

