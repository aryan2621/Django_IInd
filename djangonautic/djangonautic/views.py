from django.http import HttpResponse
from django.shortcuts import render

def about(req):
  # return HttpResponse('about')
  return render(req, 'about.html')

def home(req):
  return render(req, 'homepage.html')