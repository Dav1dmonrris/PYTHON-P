"""numero_uno=5
if numero_uno==5:
    print("El numero es 5")

print("Fin")"""


#Ejercicio 2
print("Vamos a calificar tu promedio, campeon")
nombre=input("¿Cual es tu nombre?")

print("Hola", nombre + ", Vamos a calcular tu promedio")

mate=int(input(nombre +", ¿Cual es tu promedio en matematicas?"))

esp=int(input(nombre +", ¿Cual es tu promedio en español"))

quimica=int(input(nombre +", ¿Cual es tu promedio en quimica?"))

resultado=(mate + esp + quimica)/3
if resultado>=6:
    print("Aprobaste con:", float(resultado))

print("Fin.")
