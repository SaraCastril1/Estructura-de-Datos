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
      return self.arregloDeListas[source-1][destination-1] #Solo la segunda Componente
      

    def getSuccessors(self, vertice):
        for i in range(0,vertice):
            successors = self.arregloDeListas
            return successors
       


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
#print(graph.getWeight(1,1))
print("Successors: ")
print(graph.getSuccessors(4))


