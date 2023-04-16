miLista=["ivan", "Sergio", "+", "Blanca", "Lucero"]
print(miLista[:])
print(miLista[-3])
print(miLista[3])
print(miLista[0:2])
print(miLista[:3])
print(miLista[2:])
miLista.append("+")    #se agrega al final
miLista.insert(3,"**")  #Agrega en la posicion 3 el texto
miLista.extend(["Nicol", "Valentina"])  #Agregaga al final los siguientes datos
print(miLista[:])
print(miLista.index("Valentina"))   #Busca la posicion de la palabra indicada
print("ivan" in miLista)    #para verificar si se encuentra en la lista
print("Ivan" in miLista)    #para verificar si se encuentra en la lista
print("Agregamos qwer")
miLista.append("qwer")
print(miLista[:])
print("Se remueve o elimina")
miLista.remove("qwer")
print(miLista[:])
m1=[1,2,3,4,5]
m2=[6,7,8,9,10]
m3=m1+m2            #Suma de listas
print(m3[:])