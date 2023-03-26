"""edad=int(input("Introduce edad"))

while edad<0:
    print("Introduce una edad valida")
    edad = int(input("Introduce edad"))
print("Termino la ejecucion")"""
import math
print("Programa de rais cuadrada")
numero=int(input("Introduce un numero por favor: "))

intentos=0
while numero<0:
    print("No se puede hallar la rais de un numero negativo")
    if intentos==2:
        print("Numero de intentos sobrepasados")
        break
    numero = int(input("Introduce un numero por favor: "))
    if numero<0:
        intentos=intentos+1
if intentos<2:
    solucion=math.sqrt(numero)
    print("la rais cuadrada de "+str(numero)+ "es "+str(solucion))
