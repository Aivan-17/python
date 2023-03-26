"""for i in range(5,50,3):      #range(inicio, Fin, intervalo)
    print(f"valor de la variable {i}")"""
valido=False
email=input("Introduce tu email: ")
print(len(email))
for i in range(len(email)):
    if email[i]=="@":
        valido=True

if valido:
    print("Correcto")
else:
    print("Incorrecto")