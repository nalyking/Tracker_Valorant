from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def home(request):
    return HttpResponse("Pagina Home Tracker")

