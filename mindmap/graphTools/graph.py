from ..models import Idea
from .node import Node
from .edge import Edge

class Graph:

    def __init__(self, rootNodeLabel=None, width=None, height=None):

        
        self.nodes = []
        self.edges = [] 

        rootIdea = Idea.nodes.get_or_none(label=rootNodeLabel)

        if rootIdea:
            rootNode = Node(id=rootIdea.id, label=rootIdea.label, description=rootIdea.description)
            self.nodes.append(rootNode)

        else: 
            raise Exception 


        for child in rootIdea.children.all():

            node = Node(id=child.id, label=child.label, description=child.description)
            edge = Edge(node1=rootNode, node2=node)

            self.nodes.append(node)
            self.edges.append(edge)

     
