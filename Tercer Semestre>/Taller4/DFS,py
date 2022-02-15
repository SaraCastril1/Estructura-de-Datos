from collections import deque

class GraphAL:
    def __init__(self, size):
      self.arregloDeListas = [0]*size
        #[size]
        #[ [], [], [], [] , [] ,[] ...]

      for i in range(0, size):
        self.arregloDeListas[i]= deque()
  
        
    def addArc(self, vertex, destination, weight):
       fila = self.arregloDeListas[vertex]
       arco = (destination,weight)
       fila.append(arco)
        
    def getWeight(self, source, destination):   
      return self.arregloDeListas[source][destination] 
      

    def getSuccessors(self, vertice):
      successors = self.arregloDeListas[vertice]
      return successors

    
def path(graph,size,source:int,dest:int)->bool:
  visited = [False]*size #My hash table of visited vertices.
                                     #[ [False], [False], [False], [False]  ...]
  return path_AUX(graph, source, dest, visited)
      
def path_AUX(graph, source:int, dest:int, visited)->bool:
  visited[source] = True
  if source == dest: 
    return True
  else:
    for nextV in graph.getSuccessors(source): 
      if not visited[nextV[0]]: 
        pathFrom_nextV_to_dest = path_AUX(graph,nextV[0],dest, visited)
        if pathFrom_nextV_to_dest:
          return True
  return False

    



size = 7
graph = GraphAL(size)

graph.addArc(0,0,1)
graph.addArc(0,1,1)
graph.addArc(1,2,1)
graph.addArc(1,5,1)
graph.addArc(2,1,1) 
graph.addArc(2,5,1)
graph.addArc(2,3,1)
graph.addArc(3,4,1)
graph.addArc(4,0,1)
graph.addArc(4,5,1)

print(graph.arregloDeListas)
print("\n")
print(graph.getSuccessors(0))
print(graph.getSuccessors(0)[0][0])

 
print(path(graph,size,0,4))  #True
print(path(graph,size,1,3)) #True
print(path(graph,size,0,0)) #True
print(path(graph,size,5,3)) #False
print(path(graph,size,0,6)) #False
