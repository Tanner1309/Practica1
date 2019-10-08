#Se importa el modulo de matematicas
import math
#Se importa numpy como la palabra np 
import numpy as np
#Se importa matplotlib como la palabra plt 
import matplotlib.pyplot as plt
#se piden los datos necesario
print("Este programa resuelve ecuaciones cuadraticas de la forma AX^2 + BX + C ")
A=int(input("Inserte el valor de A: "))
B=int(input("Inserte el valor de B: "))
C=int(input("Inserte el valor de C: "))
xr=int(input("Inserte el primer punto: "))
#se obtiene el primer valor
xr=math.sqrt((-B*xr-C)/A)
#se declara la lista donde se guardaran los valores de los errores 
ve=[]
c=0
while True:
    #se guarda el valor de xr para calcular el error
    xra=xr
    xrn=math.sqrt((-B*xr-C)/A)
    #se evalua el error
    e=math.fabs(xra-xrn)
    ve.append(e)
    if e <= 0.000001 or e == 0.0:
        break
    xr=xrn
    c=c+1
#se muestra el grafico de error
#se pasa la lista a arreglo
vecE=np.array(ve)
#se obtiene el tamano del vector 
x= vecE.size
#se crea el vector x
vecX=np.arange(0,x)
print("El resultado mas cercano es:",xr)
#se hace la grafica
plt.plot(vecX,vecE, "go--", linewidth=2, markersize=5)
#se muestra la grafica
plt.show()
plt.savefig("Metodo3.png")