#Funcion len()

#Primera opcion
print("Hola tiene ", len("hola"), "caracteres")
#segunda opcion
longitud=len("paragaricutirimicuaro")
print("La longitud de parangaricutirimicuaro es: ", longitud, "caracteres")

#metodos strip()
"""Elimina los elementos que coincidan en el inicio el el final de la cadena"""
cadena=" Hola mundo "
cadenaa=cadena.strip("s Hol")
print(cadenaa)

#metodos lstrip()
"""Elimina los elementos que coincidan al inicio de la cadena"""
cadena=" Hola mundo "
cadenaa=cadena.lstrip("s Hol")
print(cadenaa)


#metodos rstrip()
"""Elimina los elementos que coincidan al final de la cadena"""
cadena=" Hola mundo "
cadenaa=cadena.rstrip("s Hol")
print(cadenaa)

#metodos istitle()
"""Consulta si la cadena esta correctamente escrita true - false"""
cadena=" HoLa muNDo "
print(cadena.istitle())


#metodos title()
"""Cambia la cadena a la correcta forma"""
cadena=" HoLa muNDo "
cadenaa=cadena.title()
print(cadenaa)

