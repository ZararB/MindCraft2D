from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Idea 

# Create your views here.

def index(request):

    return HttpResponse("Hello World")

def mindmap(request, rootNodeTitle):
    
    rootNode = Idea.nodes.get(title=rootNodeTitle)
    
    # Visualize graph


    return render(request, 'mindmap/mindmap.html', {'nodes':'rootNode'})

