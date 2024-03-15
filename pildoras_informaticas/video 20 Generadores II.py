#practica generadores II
def devuelve_ciudades(*ciudades):

    #el * antes del valor que se enviara en este caso "*ciudades" esta
    #informando a la funcion que resivira distitas cantidades de elementos
    #como podria ser 1 hasta infinito
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento
    #     Segunda manera
    # for elemento in ciudades:
    #     #for subElemento in elemento:
    #         yield from elemento
        # Yield se utiliza en las funciones generadoras que son funciones
        # iguales a los iteradores es decir, podemos iterar sobre ellas, pero
        # la diferencia con los iteradores es que se pueden crear de forma más
        # sencilla. Estas se valen de la sentencia yield que es muy similar a
        # return, pero con la diferencia de que podemos usarlo varias veces en
        # una misma función.
ciudades_devueltas=devuelve_ciudades("Madrid","La Paz","Mexico","Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))