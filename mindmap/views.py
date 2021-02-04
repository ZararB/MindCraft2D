from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Idea 

# Create your views here.

def index(request):
    da = str(type(request))

    return HttpResponse("Hello")



def mindmap(request, rootNodeTitle):
    
    rootNode = Idea.nodes.get(title=rootNodeTitle)
    
    # Visualize graph

    context = {'nodes':nodes}

    return render(request, 'mindmap/mindmap.html', context)


def addNodeForm(request):

    return render(request, 'mindmap/learning.html') 

def addNode(request):

    pass
