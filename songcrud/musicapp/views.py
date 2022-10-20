from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def index(response):
    return HttpResponse("<h1>Hello World</h1>")

def next(response):
    return HttpResponse("<h2>You are welcomed to my World</h2>")