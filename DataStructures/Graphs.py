### Edge List
## shows the connections, for example, [ 0 is connected to 2, 2 is connected to 0 ]
# graph = [ [0, 2], [2, 3], [2, 1], [1, 3] ]

# ### Adjacent List
# ## 
# graph = [ [2], [2,3], [0,1,3], [1,2] ]
# graph = {
#     0: [2],
#     1: [2, 3],
#     2: [0, 1, 3],
#     3: [1, 2]
# }

# ### Adjacent Matrix
# ## 0 is connected to 2
# ## 1 is connected to 2 & 3 .....
# graph = {
#     0: [0, 0, 1, 0],
#     1: [0, 0, 1, 1],
#     2: [1, 1, 0, 1],
#     3: [0, 1, 1, 0]
# }

class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}
        
    def addVertex(self, node):
        self.adjacentList[node] = []
        self.numberOfNodes += 1
        return self
        
    def addEdge(self, node1, node2):
        ## undirected graph -- node1 is connected to node2, node2 is connected to node1
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
        return self
    
    def showConnections(self):
        allNodes = list(self.adjacentList.keys())
        for node in allNodes:
            nodeConnections = self.adjacentList[node]
            connections = "  ".join(str(vertex) for vertex in nodeConnections)
            print(node + " --> " + connections)
    
myGraph = Graph()
### Adding Nodes
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')

### Adding Connections between the Nodes
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4') 
myGraph.addEdge('4', '2') 
myGraph.addEdge('4', '5') 
myGraph.addEdge('1', '2') 
myGraph.addEdge('1', '0') 
myGraph.addEdge('0', '2') 
myGraph.addEdge('6', '5')

myGraph.showConnections()