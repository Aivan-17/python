"""Condicional
    instruccion IF"""
print("Programa de evaluacion de notas de alumnos")
nota_alum=input()
def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="Suspendido"
    return valoracion
print(evaluacion(int(nota_alum)))
