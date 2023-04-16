""" -Son estructuras que extraen valores de una funcion y se almacenan en objetos iterables (que se pueden recorrer).
    *Estos valores se almacenan de uno en uno
    * Cada ves que un generador almacena un valor, esta permanece en un estado pausado hasta que se solicita el siguiente. Esta caracteristica es conocida como "Suspension de estado"
    """
def generaPares(limite):
    num=1
    #milista=[]
    while num<limite:
        yield num*2
        #milista.append(num*2)
        num=num+1
devuelvePares=generaPares(10)
#print(generaPares(10))
for i in devuelvePares:
    print(i)

