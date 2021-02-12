from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Idea 
from .graphTools import GraphVisualization
from .graphTools.graph import Graph 
from django.shortcuts import redirect
import json 

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

def deleteNode(request):

    data = json.loads(request.body) 
    
    uid = data['nodeId'][:-14]
    rootNodeLabel = data['rootNodeLabel']
    node = Idea.nodes.get_or_none(uid=uid)

    if node:
        node.delete()

    graph = Graph('Existence').toJson()

    return HttpResponse(graph, content_type='application/json')




def save(request):

    rootNodeLabel = request.POST['rootNodeLabel']
    
    node = Idea(label=rootNodeLabel)
    node.save()

    return redirect('/' + rootNodeLabel)

def setupDb(request):

    rootNode = Idea(label="Existence").save()

    projects = Idea(label="Projects").save()

    adminAccess = Idea(label="Admin Access").save()

    rootNode.children.connect(projects)
    rootNode.children.connect(adminAccess)

    return redirect('/Existence')


def mindmap(request, rootNodeLabel):

    
    graph = Graph(rootNodeLabel)
    GraphVisualization.orbital_visualization(graph)
    
    

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