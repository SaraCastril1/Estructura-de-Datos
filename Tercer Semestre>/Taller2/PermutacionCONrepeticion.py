#---------------- Permutaciones con repetición (Infinita) --------------------
# -----------------    Importa el orden ----------------------------

def permutacion(cadena):
   permutacionAux(cadena, "")

def permutacionAux(pregunta, respuesta):
   if len(respuesta)== len(pregunta): #También puedo usar un valor n
      print(respuesta)
   else:
      for i in range (0, len(pregunta)):
         permutacionAux(pregunta, respuesta+pregunta[i])



def permutacion_arreglo(cadena):
   lista = []
   permutacion_arreglo_aux(cadena,"", lista)
   return lista

def permutacion_arreglo_aux(pregunta, respuesta, lista):
   if len(pregunta)== len(respuesta):
      lista.append(respuesta)
   else:
      for i in range (0, len(pregunta)):
         permutacion_arreglo_aux(pregunta, respuesta+pregunta[i], lista)


def main():
   permutacion("ABC")
   print(permutacion_arreglo("ABC"))

main()
