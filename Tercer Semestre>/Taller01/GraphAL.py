from collections import deque

class GraphAL:
    def __init__(self, size):
      self.arregloDeListas = [0]*size
        #[size]
        #[ [], [], [], [] , [] ,[] ...]

      for i in range(0, size):
        self.arregloDeListas[i]= deque()
  
        
    def addArc(self, vertex, destination, weight):
       fila = self.arregloDeListas[vertex-1]
       arco = (destination,weight)
       fila.append(arco)
        
    def getWeight(self, source, destination):   
      return self.arregloDeListas[source-1][destination-1] 
      

    def getSuccessors(self, vertice):
      successors = self.arregloDeListas[vertice-1]
      return successors

    def verify_path(self):
      print("Check if there is a path from point A to point B")
      A = int(input("Point A: "))
      B = int(input("Point B: "))
      if self.getSuccessors(A) is not None: 
        if self.arregloDeListas[A][0] == B:
          print("True")
      else: print("False")
      

size = int(input("Número de vértices del grafo:"))
n_edges =int(input("Número de aristas del grafo:")) 
graph = GraphAL(size)
print(graph.arregloDeListas)


for i in range (n_edges):
  source = int(input("Origen: ")) 
  destination = int(input("Destino: "))
  weight = int(input("Peso: "))

  graph.addArc(source, destination, weight)

print(graph.arregloDeListas)
print(graph.verify_path())

