from . import graph
import math


def orbital_visualization(graph, width=1920, height=1080, radius=200):
    '''
    Adds the appropriate cordinates to the nodes and edges in graph
    Uses a simple orbital pattern for visualization
    '''

    origin_x = width / 2 
    origin_y = height / 2 

    rootNode = graph.nodes[0]
    rootNode.cx = str(origin_x) + 'px' 
    rootNode.cy = str(origin_y) + 'px' 

    

    children = graph.nodes[1:]

    if len(children) > 0:

        num_children = len(children)

        children_per_shell = 8

        num_shells = math.ceil(num_children / children_per_shell)


        delta = 360 / (num_children)

        offset = 0

        for shell in range(num_shells):

            for i, child in enumerate(children[shell*children_per_shell:(shell+1)*children_per_shell]):
                
                radius = radius*(shell+1)

                angle_from_positive_x = offset + (num_shells-1)*delta + delta*i

                child.cx = str(origin_x + math.cos(angle_from_positive_x)*radius) + 'px'
                child.cy = str(origin_y - math.sin(angle_from_positive_x)*radius) + 'px'

            offset += delta

        for edge in graph.edges:

            edge.x1 = edge.node1.cx
            edge.y1 = edge.node1.cy
            edge.x2 = edge.node2.cx
            edge.y2 = edge.node2.cy

