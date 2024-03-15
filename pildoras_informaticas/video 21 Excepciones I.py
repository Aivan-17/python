# #Una excepcio son errores que ocurren durante la ejecucion del
# programa. La sintaxis del codigo es correcta pero durante la ejecucion
# ha ocurrido "Algo inesperado"
# Este tipo de errores de ejecucion se pueden controlar para que la ejecucion
# del programa continue.Es lo que se conoce como manejo o control de excepciones.
def suma (num1, num2):
     return num1 + num2
def resta  (num1, num2):
     return num1 - num2
def multiplicacion (num1, num2):
     return num1 * num2
def division (num1, num2):
     return num1 / num2
op1=(int(input("Introduce el primer numero: ")))
op2=(int(input("Introduce el segundo numero: ")))
operacion=input("Introduce la operacion a realizar (suma, resta, multiplicacion, division): ")
if operacion=="suma":
     print(suma(op1,op2))
elif operacion=="resta":
     print(resta(op1,op2))
elif operacion=="multiplicacion":
     print(multiplicacion(op1, op2))
elif operacion=="division":
     print(division(op1, op2))
else:
     print("Operacion no completada")
print("Operacion ejecutada. Continuacion de ejecucion del programa")