from django.shortcuts import render
from django.http import HttpResponse


def Tracker(request):
    return HttpResponse("Tracker Home")