#Parametros end 

"""print("Esto es un ejemplo", end='-')
print("muy practico")

#parametos sep

print( "1","2","3","4","5", sep='')"""

#fobonacci 
"""x=1
i=0

while i<=1597:
    print(i, x, end=' ')
    i=i+x
    x=i+x"""
   
#Funcion break
print("While con la sentencia break")
contador=0
while contador<10:
        contador+=1
        if contador==5:
            break
        print("Valor actial de la variable ", contador)
print("Fin del programa, la sentencia break de a ejecutado")

#Funcion continue
print("While con la sentencia continue")
contador=0
while contador<10:
        contador+=1
        if contador==5:
            continue
        print("Valor actual de la variable: ", contador)
