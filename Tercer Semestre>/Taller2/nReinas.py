

def n_reinas(n : int, cadena_ppal = "0"):
   for i in range(0, n-1):
      cadena_ppal += str(i+1)
   return cadena_ppal


def permutacion_arreglo(cadena):
   lista = []
   permutacion_arreglo_aux(cadena,"", lista)
   return lista

def permutacion_arreglo_aux(pregunta, respuesta, lista):
   if len(pregunta)== 0:
      lista.append(respuesta)
   else:
      for i in range (0, len(pregunta)):
         nuevapregunta = pregunta[0:i] + pregunta[i+1:]
         permutacion_arreglo_aux(nuevapregunta, respuesta+pregunta[i], lista)

def generar_coordenadas(lista, n):
   arreglo_de_coordenadas = []
   for i in range(0, len(lista)):
     posibilidad = []
     for j in range(0, n):
       miReina = lista[i]
       coordenada = [j,int(miReina[j])]
       posibilidad.append(coordenada)
     arreglo_de_coordenadas.append(posibilidad)
   return arreglo_de_coordenadas
   

def verificar_diagonales(arreglo_de_coordenadas):
  lista_final = []
  for i in range(0, len(arreglo_de_coordenadas)):
    unaReina =[]
    for j in range (0, len(arreglo_de_coordenadas[i])-1):
      x1 = arreglo_de_coordenadas[i][j][0]  
      x2 = arreglo_de_coordenadas[i][j+1][0]
      y1 = arreglo_de_coordenadas[i][j][1]
      y2 = arreglo_de_coordenadas[i][j+1][1]

      m = (y2**2 - y1**2)/(x2**2 - x1**2)

      if m == 1:
        continue
      else:
        unaReina.append(arreglo_de_coordenadas[i][j])
    unaReina.append(arreglo_de_coordenadas[i][j+1])
    lista_final.append(unaReina) 
      
  return lista_final

def comprimir_reinas(lista_final, n):
  for i in range(0, len(lista_final)):
    cadena = ""
    for j in range (0, len(lista_final[i])):
      cadena += str(lista_final[i][j][1]) 
    if len(cadena)==n:
      print(cadena) 



   

def main():
   n = int(input("Ingrese su número de reinas: "))
   print("\n Sin verificar diagonales: ")
   lista_permutaciones = permutacion_arreglo(n_reinas(n))
   print(permutacion_arreglo(n_reinas(n) ))
   print("\n Coordenadas de cada posibilidad: ")
   print(generar_coordenadas(lista_permutaciones, n))
   lista_de_coordenadas= (generar_coordenadas(lista_permutaciones, n))
   print("\n Las posibles posiciones de las reinas son: ") #La primera está incorrecta
   print(verificar_diagonales(lista_de_coordenadas))
   lista_final = verificar_diagonales(lista_de_coordenadas)
   print("\n TABLEROS POSIBLES PARA n = ", n)
   comprimir_reinas(lista_final, n)


main()
