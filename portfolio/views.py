from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "portfolio/index.html")

def profile(request, username):
    # send profile header info here
    return render(request, "portfolio/profile.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
