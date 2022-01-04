class Graph:
    #Constructor function to create the Graph with an adjacency list using dictionary
    def __init__ (self, dict):
        if dict is None:
            dict = {}
        self.dict = dict
    
    #Method to add edges to the graph 
    def addEdge (self, vertex, edge):
        self.dict[vertex].append[edge]
    
       