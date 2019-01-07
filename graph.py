class Graph:
    def __init__(self, V=None):
        self.V=V
        self.graph={}
        for i in range(V):
            self.graph[i]=[]
        

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printPaths(self, u, v, path, visited):
        path.append(u)
        visited[u]=True
        if u==v:
            print path
        else:
            for child in self.graph[u]:
                if visited[child]==False:
                    self.printPaths(child, v, path, visited)
        path.pop()
        visited[u]= False
        


g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(0, 3) 
g.addEdge(2, 0) 
g.addEdge(2, 1) 
g.addEdge(1, 3)

(g.printPaths(2,3,[],[False, False, False, False]))

    
