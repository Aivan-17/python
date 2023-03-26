print("programa de becas anio 2017")
distancia=int(input("Introduce la distancia a la escuela"))
print(distancia)
numeroHermanos=int(input("Introduce el n de hermanos "))
print(numeroHermanos)
salario=int(input("Introduce salario anual"))
print(salario)
if distancia>40 and numeroHermanos>2 and salario<=20000:
    print("Beca!!!")
else:
    print("NO tienes derecho a BECA!!!")