class Edge:

    def __init__(self, node1=None, node2=None):

        
        self.node1 = node1
        self.node2 = node2

        if node1 and node2:

            self.x1 = node1.cx
            self.y1 = node1.cy
            self.x2 = node2.cx
            self.y2 = node2.cy

    
