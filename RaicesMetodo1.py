#Se importa el modulo de matematicas
import math
#se piden los datos necesarios
fx=input("Inserte la funcion:")
xl=int(input("Inserte el primer limite"))
xu=int(input("Inserte el segundo limite"))
#se obtiene el primer xr

xr=(xl+xu)/2
while True:
    #se evalua en la funcion xl xu y xr 
    xra=xr
    if (fxl*fxr) > 0:
        xl=xr
    elif (fxu*fxr) > 0:
        xu=xr
    xrn=(xl+xu)/2
    e=math.fabs(xrn-xra)
    if e <= 0.1:
        break
    xr=(xl+xu)/2

