#Ejercicio de practica 
print("Bienvenido a mi empresa imaginaria")
Nombre=input("Nombre de empleado: ")
print("clave 1 - Clave 2 - Clave 3 ")
clave=int(input("Ingrese su clave: "))
antiguedad=int(input("Ingrese su antiguedad en años:"))

if clave==1:
   
    if antiguedad==1:
        print("Tiene derecho a 6 dias de vacaciones")
    elif antiguedad>=2 and antiguedad<=6:
        print("Tiene 14 dias de vacaciones")
    elif antiguedad>=7:
        print("Tiene 20 dias de vacaciones")
    else:
        print("No tiene derecho a vacaciones")

if clave==2:
    
    if antiguedad==1:
        print("Tiene derecho a 7 dias de vacaciones")
    elif antiguedad>=2 and antiguedad<=6:
        print("Tiene 15 dias de vacaciones")
    elif antiguedad>=7:
        print("Tiene 22 dias de vacaciones")
    else:
        print("No tiene derecho a vacaciones")

if clave==3:
   
    if antiguedad==1:
        print("Tiene derecho a 10 dias de vacaciones")
    elif antiguedad>=2 and antiguedad<=6:
        print("Tiene 20 dias de vacaciones")
    elif antiguedad>=7:
        print("Tiene 30 dias de vacaciones")
    else:
        print("No tiene derecho a vacaciones")
if clave>3:
    print("Su clave no existe")