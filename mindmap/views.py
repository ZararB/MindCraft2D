from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Idea 
from .graphTools import graphVisualizer
from .graphTools.graph import Graph 
from django.shortcuts import redirect

def index(request):
    return render(request, 'mindmap/index.html')

def new(request):
    return render(request, 'mindmap/new.html')

def load(request):
    return render(request, 'mindmap/load.html')

def learning(request):
    return render(request, 'mindmap/learning.html')
    
def settings(request):
    return render(request, 'mindmap/settings.html')

def open(request):

    rootNodeLabel = request.GET['rootNodeLabel']

    #TODO Check if node exists and handle accordingly

    return redirect('/' + rootNodeLabel)

def delete(request):

    nodeId = int(request.POST['nodeId'])
    rootNodeLabel = request.POST['rootNodeLabel']
    node = Idea.nodes.get_or_none(id=nodeId)

    if node:
        node.delete()

    return redirect('/' + rootNodeLabel)



def save(request):

    rootNodeLabel = request.POST['rootNodeLabel']
    
    node = Idea(label=rootNodeLabel)
    node.save()

    return redirect('/' + rootNodeLabel)



def mindmap(request, rootNodeLabel):

    '''
    
    ''' 
    graph = Graph(rootNodeLabel)
    graphVisualizer.orbital_visualization(graph)
    
    

    context = {"graph":graph, "rootNodeLabel": graph.nodes[0].label}
    return render(request, 'mindmap/mindmap.html', context)

'''


def addNode(request):
    pass

def deleteNode(request):
    pass

def updateNode(request):
    pass

'''