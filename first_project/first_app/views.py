from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("<em>Hello World!</em>")

def home(response):
    return HttpResponse("Welcome Home!")