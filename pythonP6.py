#operadores logicos
numero_uno=int(input("Escribe el primer numero"))
numero_dos=int(input("Escribe el segundo numero"))

#conjuncion "and"
if numero_uno==5 and numero_dos>=5:
    print("Las dos condiciones se cumplieron")
else:
    print("Una condicion o nunguna se cumplio")
#Disyuncion "or"
if numero_uno==5 or numero_dos>=5:
    print("Una de las condiciones se cumplio")
else:
    print("Ninguna condicion se cumplio")

#Negacion "not"
if not numero_uno==5:
    print("El numero no es igual a 5")
else:
    print("el numero es 5")
