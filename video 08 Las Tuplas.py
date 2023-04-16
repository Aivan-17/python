"""
Que son las tuplas
    *Las tuplas sin listas inmutables, es decir, no se pueden modificar despues de su creacion
        *No permiten aniadir, eliminar, mover elementos etc(no append, extend, remove)
        *Si permiten extraer porciones, pero el resultado de la extraccion es una tupla nueva.
        *No permiten busquedas(no index).
        *Si permiten comprobar si un elemento se encuentra en la tupla.
    *Que utilidad o ventaja tienen respecto a las listas?
        *Mas rapidas
        *Menos espacio(mayor optimisacion)
        *formatean Strings
        *Pueden utilisarse como claves en un diccionario. (las listas no)
        la diferencia de la sintaxis es la siguiente:
        nombreLista=[elem1,elem2,elem3....]------> es una lista que esta entre corchetes []
        nombreTupla=(elem1, elem2, elem3 ......)-----> es una tupla que esta entre parentesis ()
"""
mitupla=("Ivan",13,1,1994)
miLista=list(mitupla)       #cambia de una tupla a una lista
print(mitupla[1])
print(miLista)
print(mitupla)
ml1=["juan",13,1,13,1994,13,2,13,13,5]
mt1=tuple(ml1)          #cambia de una lista a tupla
print(mt1.count(13))    #Cuenta cuantas veces esta en la tupla el numero o elemento puesto en este caso es el "13"
print(len(mt1))         #Cuenta cuantos elementos esta en la tupla
mitupplafecha=("Febrero",17,2,1994)
"""mitupplafecha.append("Ivan")"""
nombre, dia, mes, anio=mitupplafecha
print("nombre:" ,nombre)
print("dia:",dia)
print("mes:",mes)
print("anio:",anio)