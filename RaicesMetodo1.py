#Se importa el modulo de matematicas
import math
import numpy as np
import matplotlib.pyplot as plt
#se piden los datos necesario
print("Este programa resuelve ecuaciones cuadraticas de la forma AX^2 + BX + C ")
A=input("Inserte el valor de A:")
B=input("Inserte el valor de B: ")
C=input("Inserte el valor de C: ")
xl=float(input("Inserte el primer limite: "))
xu=float(input("Inserte el segundo limite: "))
#se obtiene el primer xr
xr=float((xl+xu)/2)
c=0
ve=[]
while True:
    #se evalua en la funcion xl xu y xr
    fxl=float(A*(xl*xl)+B*xl+C)
    fxr=float(A*(xr*xr)+B*xr+C)
    fxu=float(A*(xu*xu)+B*xu+C)
    #se guarda el valor de xr para calcular el error
    xra=xr
    if (fxl*fxr) > 0:
        xl=xr
    elif (fxu*fxr) > 0:
        xu=xr
    xrn=(xl+xu)/2
    e=math.fabs(xrn-xra)
    ve.append(e)
    if e <= 0.1:
        break
    xr=(xl+xu)/2
    c=c+1    
#se muestra el grafico de error
vecE=np.array(ve)
vecC=np.array(0,c)
plt.plot(vecC,vecE)
plt.show()

