from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return HttpResponse(" <h1> Home </h1>")


def home(response):
    return render(response,'main/homepage.html')

def find(response):
    return render(response,'main/find.html')

def play(response):
    return render(response,'main/play.html')

# Create your views here.
