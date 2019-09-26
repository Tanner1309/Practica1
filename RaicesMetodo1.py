#Se importa el modulo de matematicas
import math
import numpy as np
import matplotlib.pyplot as plt
#se piden los datos necesario
print("Este programa resuelve ecuaciones cuadraticas de la forma AX^2 + BX + C ")
A=int(input("Inserte el valor de A:"))
B=int(input("Inserte el valor de B: "))
C=int(input("Inserte el valor de C: "))
xl=int(input("Inserte el primer limite: "))
xu=int(input("Inserte el segundo limite: "))
#se obtiene el primer xr
xr=(xl+xu)/2

ve=[]
while True:
    #se evalua en la funcion xl xu y xr
    fxl=A*(xl*xl)+B*xl+C
    fxr=A*(xr*xr)+B*xr+C
    fxu=A*(xu*xu)+B*xu+C
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
   
#se muestra el grafico de error
vecE=np.array(ve)
x= vecE.size
vecX=np.arange(0,x)
plt.plot(vecX,vecE)
plt.show()

