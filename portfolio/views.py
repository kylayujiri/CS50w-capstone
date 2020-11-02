import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Artist, Work, Comment, Album, Category

# Create your views here.
def index(request):
    return render(request, "portfolio/index.html")


def profile(request, username):
    # send profile header info here
    return render(request, "portfolio/profile.html")


def edit_profile(request, username):
    pass


@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        confirm = data.get("confirm")

        # ensure password matches confirmation
        if password != confirm:
            return JsonResponse({"message": "Passwords must match."})

        try:
            new_artist = Artist.objects.create_user(username, email, password)
            new_artist.save()
        except IntegrityError:
            return JsonResponse({"message": "Username already taken."})

        login(request, new_artist)
        return JsonResponse({"message": "User created successfully."}, status=201)

    else:
        return JsonResponse({"error": "POST request required."}, status=400)


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        artist = authenticate(request, username=username, password=password)

        if artist is not None:
            login(request, artist)
            return JsonResponse({"message": "User logged in successfully."}, status=201)
        else:
            return JsonResponse({"message": "Invalid username and/or password."})
    else:
        return JsonResponse({"error": "POST request required."}, status=400)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
