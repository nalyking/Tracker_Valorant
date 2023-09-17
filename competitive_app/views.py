from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def register(request):
    return HttpResponse(json.dumps({
        "nome":"BM Arion",
        "Hashtag":"60hz",
    }))

def home(request):
    return HttpResponse("Pagina Home Tracker")

def login(request):
    return HttpResponse(json.dumps({
        "user_name": "user_name",
        "password": "password",
        "save": "save",
    }))