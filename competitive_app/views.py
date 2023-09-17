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
    return HttpResponse(json.dumps({
        "vc esta na tela de home":"home"
    }))