"""
ojo no permite busqueda (no index) a partir del 3.06 si se puede
Los Diccionarios
*Estrucura de datos que nos permite almacenar valores de diferente tipo (enteros, cadenas de testo, decimales)
e incluso listas y otros diccionarios
* La principal caracteristica de los diccionarios es que los datos se almacenan asociados a una clave de tal forma que se crea una asociacion de clave : valor
para cada elemento almacenado.
* Los elementos almacenados no estan ordenados. El orden es indiferente a la hora de almacenar informacion en un diccionario.
"""
diccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","Espania":"Madrid"}
print(diccionario["Francia"])
print(diccionario)
diccionario["Italia"]="Lisboa" #agrega valor
print(diccionario)
diccionario["Italia"]="Roma"    #modifica
print(diccionario)
del diccionario["Reino Unido"]  #se elimina
print(diccionario)
dic2={"Al":"berlin",23:"Aivan","Sergio":17}     #Las formas de guardar
print(dic2)

tupla=["es","fr","ru","al"]
midic={tupla[0]:"madrid",tupla[1]:"paris",tupla[2]:"londres",tupla[3]:"berlin"}
print(midic)
md3={"equipo":"chicago","anillos":{"temp":[1991,1992,1993]}}    #Se puede hacer eso pero no es practico

print(diccionario.keys())       #saca las llaves del,diccionario
print(diccionario.values())     #saca los valores del diccionario
print(len(diccionario))