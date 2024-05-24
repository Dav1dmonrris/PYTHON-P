#clase Range()
"""for indice in range(0, 11, 2):
    print(indice)
print("Fin del programa")"""

"""tabla=int(input("¿Que tabla de multiplicar quieres?"))
print("--------------")
for cantidad in range(0,11):
    resultado=cantidad*tabla

    print(cantidad , " x " , tabla , "= " , resultado)
print("--------------")"""
#video 47
vocales=["a", "e","i", "o","u"]
print("Las vocales son: ", vocales)
nueva_vocal=int(input("¿Cual vocal quieres remplazar?"))
vocales[nueva_vocal]= input("¿Por cual desea combiarla?")
for indice in vocales:
    print(indice)

print("¿Desea agregar otro elemento? Si o No")
eleccion=input("")
if eleccion=="si" or eleccion=="Si":
     vocales.append(input("¿Que elemento desea agregar?"))
else:
     print("Gracias por participar")
print("Su nueva lista es:")
for indice in vocales:
     print(indice, end=" ,")
#Funcion append(),insert(), pop(), remove().
#Instruccion "del()" se utiliza para eliminar una lista o elementos de una 
#metodo Lista.reverse(), invierte los valores de la lista
#Metodo Lista.sort(), Ordena la lista
#Metodo Index(), Buscar un elemento en una lista
#Video 52
    