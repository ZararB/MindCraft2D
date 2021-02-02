from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Idea 

# Create your views here.

def index(request):

    return HttpResponse("Hello World")

def mindmap(request, rootNode):
    
    return HttpResponse(rootNode)
