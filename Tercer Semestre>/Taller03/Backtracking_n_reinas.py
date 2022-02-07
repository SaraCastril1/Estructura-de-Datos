import numpy as np

def n_reinas(n:int):
  n_reinas_aux(n, 0, [0]*n) #[0]*n ---> Crea una lista con n ceros


def n_reinas_aux(n:int, c:int, tablero:list):
  if c==n:
    print(tablero)
  
  else:
    for row in range(n):
      tablero[c] = row  #Empieze a probar

    if se_atacan_hastaI(tablero, c):
      pass                       #No la tenga en cuenta
    else:
      n_reinas_aux(n, c+1, tablero)
    

def se_atacan_hastaI(tablero: list, i:int):
  ataque = False
  for j in range(0,i):
    for k in range(j+1, i):
      if np.abs(tablero[j]-tablero[k]) == np.abs(j-k) or tablero[j]==tablero[k] :
        ataque = True
  return ataque


    
def main():
  n= int(input("Número de reinas: "))
  n_reinas(n)

main()
