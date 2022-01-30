import numpy as np

class GraphAm:
    def __init__(self, size):
         self.matriz = np.zeros((size,size))

    def getWeight(self, source, destination):
      return int(self.matriz[source-1][destination-1])

    def addArc(self, source, destination, weight):
      self.matriz[source-1][destination-1] = weight

    #def getSuccessors(self, vertex):
     #   filaVertice = self.matriz[vertex]
      #  respuesta = []
       # for j in range(0,len(self.matriz)):
        #    if filaVertice[j] != 0:
         #       respuesta.append(j)
        #return respuesta


size = int(input("Número de vértices del grafo:"))
n_edges =int(input("Número de aristas del grafo:")) 
graph = GraphAm(size)
print(graph.matriz)


for i in range (n_edges):
  source = int(input("Origen: ")) 
  destination = int(input("Destino: "))
  weight = int(input("Peso: "))

  graph.addArc(source, destination, weight)

print(graph.matriz)
print(graph.getWeight(1,1))
#print("Successors: 1")
#print(graph.getSuccessors(4))
