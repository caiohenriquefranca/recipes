from django.shortcuts import render
from django.http import HttpResponse  # noqa: F401


def home(request):
    return render(request, "recipes/pages/home.html")


def recipe(request, id):
    return render(request, "recipes/pages/recipe-view.html")
