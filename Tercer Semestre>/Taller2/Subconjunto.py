def subconjuntos(cadena):
   subconjuntosAux(cadena," " )

def subconjuntosAux(pregunta, respuesta):
   if len(pregunta)== 0:
      print(respuesta)
   else:
      subconjuntosAux(pregunta[1:], respuesta+pregunta[0] ) 
      subconjuntosAux(pregunta[1:], respuesta) 


def subconjuntos_arreglo(cadena):
   lista = []
   subconjuntos_arreglo_aux(cadena," ", lista )
   return lista

def subconjuntos_arreglo_aux(pregunta, respuesta,lista):
   if len(pregunta)== 0:
      lista.append(respuesta)
   else:
      subconjuntos_arreglo_aux(pregunta[1:], respuesta+pregunta[0], lista) 
      subconjuntos_arreglo_aux(pregunta[1:], respuesta, lista) 

def main():
   subconjuntos("ABC")
   print(subconjuntos_arreglo("ABC"))

main()
