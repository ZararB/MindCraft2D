from ..models import Idea
from .node import Node
from .edge import Edge
import json 

class Graph:

    def __init__(self, rootNodeUid=None, rootNodeLabel=None, width=None, height=None):

        
        self.nodes = []
        self.edges = [] 

        rootIdea = Idea.nodes.get_or_none(label="Existence")

        if rootIdea:
            rootNode = Node(uid=rootIdea.uid, label=rootIdea.label, description=rootIdea.description)
            self.nodes.append(rootNode)

        else: 
            raise Exception 


        for child in rootIdea.children.all():

            node = Node(uid=child.uid, label=child.label, description=child.description)
            edge = Edge(node1=rootNode, node2=node)

            self.nodes.append(node)
            self.edges.append(edge)


    #TODO Convert graph to dictionary or json for http reponses
     
    def toJson(self):

        graph = {'nodes': [], 'edges': []}

        for i, node in enumerate(self.nodes):

            nodeDict = {
                'uid': node.uid,
                'label': node.label,
                'description': node.description,
                'cx': node.cx,
                'cy': node.cy,
                'r': node.r
            }

            graph['nodes'].append(nodeDict)

        for i, edge in enumerate(self.edges):
            
            edgeDict = {
                'x1': edge.x1,
                'y1': edge.y1,
                'x2': edge.x2,
                'y2': edge.y2
            }

            graph['edges'].append(edgeDict)

        return json.dumps(graph)