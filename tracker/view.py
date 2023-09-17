from django.shortcuts import render
from django.http import HttpResponse
import json


def Tracker(request):
    return HttpResponse("Tracker Home")