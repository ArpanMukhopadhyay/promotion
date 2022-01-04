class Graph:
    #Constructor function to create the Graph with an adjacency list using dictionary
    def __init__ (self, graph):
        if graph is None:
            graph = {}
        self.graph = graph
    
    #Method to add edges to the graph 
    def addEdge (self, vertex, edge):
        self.graph[vertex].append[edge]

#BfS
visited = []
queue = []

def bfs (visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        deVertex = queue.pop(0)
        print (deVertex)

        for neighbour in  graph[deVertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)



#DFS   
visited = set()
def dfs (node, graph, visited):
    if node not in visited:
        print (node)
        visited.add(node)
        for adjacent in graph[node]:
            dfs (visited, graph, adjacent)


graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
