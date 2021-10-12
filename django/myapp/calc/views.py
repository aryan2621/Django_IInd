from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Navin'})

def add(request):
    valu1=int(request.POST['num1'])
    valu2=int(request.POST['num2'])
    res =valu1+valu2
    
    return render(request,'result.html',{'result':res})