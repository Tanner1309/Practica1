#Se importa el modulo de matematicas
import math
#Se importa numpy como la palabra np 
import numpy as np
#Se importa matplotlib como la palabra plt 
import matplotlib.pyplot as plt
#se piden los datos necesario
print("Este programa resuelve ecuaciones cuadraticas de la forma AX^2 + BX + C ")
A=int(input("Inserte el valor de A:"))
B=int(input("Inserte el valor de B: "))
C=int(input("Inserte el valor de C: "))
xr=int(input("Inserte el primer punto: "))
#se obtiene el primer xr
xr=math.sqrt(((xr+5)/2))
#se declara la lista donde se guardaran los valores de los errores 
ve=[]
c=0
while True:
    #se guarda el valor de xr para calcular el error
    xra=xr
    xrn=math.sqrt(((xr+5)/2))
    #se evalua el error
    e=math.fabs(xrn-xra)
    ve.append(e)
    if e <= 0.01:
        break
    elif e>1:
        print("El metodo no funciona por que diverge")
        break
    xrn=xr
    c=c+1
    print (c)
#se muestra el grafico de error
#se pasa la lista a arreglo
vecE=np.array(ve)
#se obtiene el tamano del vector 
x= vecE.size
#se crea el vector x
vecX=np.arange(0,x)
print("El resultado mas cercano es:",xr)
#se hace la grafica
plt.plot(vecX,vecE)
#se muestra la grafica
plt.show()
plt.savefig("Metodo2.png")