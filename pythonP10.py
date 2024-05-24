#metodo center(), ljust() y rjust().
"""numero_uno="Menu"
print(numero_uno.center(10))

numero_uno="Menu"
print(numero_uno.ljust(10))

numero_uno="Menu"
print(numero_uno.rjust(10))"""

#metodo count() para contar las veces que se repite un caracter
numero_uno="Menu"
print(numero_uno.count("u"))

#Ejercicio 2 
"""cadena=input("Escribe una frase: ")
eliminar=input("¿Que palabra eliminaras? ")
palabra=cadena.find(eliminar)
cadena.count(eliminar)
palabra_lista= cadena[0:palabra] + cadena[palabra + len(eliminar)]
print(palabra_lista, end='')"""

#Bucle for video39

palabra=input("Introduce una oracion")
palabra_alreves=""
for caracter in palabra:
    palabra_alreves=caracter+palabra_alreves
    print(palabra_alreves)