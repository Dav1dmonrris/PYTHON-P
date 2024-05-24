#condiciones multiples 
"""numero_uno=5
if numero_uno==6:
    print("El numero es 6")

elif numero_uno<=4:
    print("El numero es menor a 4")

else:
    print("Ninguna de las anteriores")"""

#condiciones anidadas
print("¿Que opcion elige?")

print("Opcion 1: convertir un numero a palabra")
print("opcion 2: convertir una palabra a numero")

opcion=int(input("¿Que opcion elige?"))

if opcion==1:
    print("¿Que numero desea convertir a palabra?")
    numero_dos=int(input())
    if numero_dos==1:
        print("Tu numero es 'Uno'")
    elif numero_dos==2:
        print("Tu numero es 'Dos'")
    elif numero_dos==3:
        print("Tu numero es 'Tres'")
elif opcion==2:
    print("¿Que palabra desea convertir a numero?")
    numero_tres=int(input())
    if numero_tres==1:
        print("Tu numero es '1'")
    elif numero_tres==2:
        print("Tu numero es '2'")
    elif numero_tres==3:
        print("Tu numero es '3'")
else:
    print("Esa opcion no existe")
print("Fin del codigo.")
