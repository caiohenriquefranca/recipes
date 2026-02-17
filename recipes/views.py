from django.shortcuts import render
from django.http import HttpResponse  # noqa: F401


def home(request):
    return render(request, "recipes/pages/home.html")



