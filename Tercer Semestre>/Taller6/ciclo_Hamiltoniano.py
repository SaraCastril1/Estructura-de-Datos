# CIRCUITO HAMILTONIANO

from collections import deque
import math

infinity = math.inf

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
        
    def getWeight(self, source, dest)->int:   
      vertex = self.getSuccessors(source)
      for i in range(0, len(vertex)):
        if vertex[i][0]==dest:
          return vertex[i][1]
      return 0
      

    def getSuccessors(self, vertice):
      successors = self.arregloDeListas[vertice]
      return successors



def cicloHamiltoniano(graph, size):
  visitados = [False]*size
  peso_menor = 9999999
  peso_total = 0
  nuevo_vertex = 0
  circuito_hamiltoniano = [0]
  
  for i in range (0, size+1):
    visitados[nuevo_vertex] = True
    #haga 1 ciclo para escoger sucesor + cerca no visitado:
    for j in graph.getSuccessors(circuito_hamiltoniano[-1]):
      candidato = j[0]
      peso_candidato = j[1]
      if visitados[candidato] == False and peso_candidato < peso_menor:
        peso_menor = j[1]
        peso_total += j[1]
        circuito_hamiltoniano.append(j[0])
        nuevo_vertex = candidato
        break

  circuito_hamiltoniano.append(0)
  print("Su circuito hamitoniano es: ", circuito_hamiltoniano, " con un costo mínimo de: ", peso_total)
      





def ciclo_Hamiltoniano_desde_cualquier_vertice(graph, v_inicial, size):
  visitados = [False]*size
  peso_menor = 9999999
  peso_total = 0
  nuevo_vertex = v_inicial
  circuito_hamiltoniano = [v_inicial]
  
  for i in range (0, size+1):
    visitados[nuevo_vertex] = True
    #haga 1 ciclo para escoger sucesor + cerca no visitado:
    for j in graph.getSuccessors(circuito_hamiltoniano[-1]):
      candidato = j[0]
      peso_candidato = j[1]
      if visitados[candidato] == False and peso_candidato < peso_menor:
        peso_menor = j[1]
        peso_total += j[1]
        circuito_hamiltoniano.append(j[0])
        nuevo_vertex = candidato
        break

  circuito_hamiltoniano.append(v_inicial)
  print("Su circuito hamitoniano es: ", circuito_hamiltoniano, " con un costo mínimo de: ", peso_total)



size = 4
graph = GraphAL(size)

graph.addArc(0,1,3)
graph.addArc(0,2,4)
graph.addArc(0,3,10)
graph.addArc(1,0,7)
graph.addArc(1,3,1)
graph.addArc(1,2,6) 
graph.addArc(2,1,2)
graph.addArc(2,0,8)
graph.addArc(2,3,9)
graph.addArc(3,2,5)
graph.addArc(3,1,11)
graph.addArc(3,0,4)
cicloHamiltoniano(graph, size)

ciclo_Hamiltoniano_desde_cualquier_vertice(graph, 3, size)
