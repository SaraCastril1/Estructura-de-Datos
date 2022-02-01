#------------ Permutaciones sin repeticiòn --------------------
# ----------------  Importa el orden --------------------------

def permutacion(cadena):
   permutacionAux(cadena, "")

def permutacionAux(pregunta, respuesta):
   if len(pregunta)== 0:
      print(respuesta)
   else:
      for i in range (0, len(pregunta)):
         nuevapregunta = pregunta[0:i] + pregunta[i+1:]
         permutacionAux(nuevapregunta, respuesta+pregunta[i])

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



def main():
   permutacion("ABC")
   print(permutacion_arreglo("ABC"))

main()
