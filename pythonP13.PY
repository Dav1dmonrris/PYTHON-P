def test_var_args(f_arg, *varia):
   print("primer argumento normal:", f_arg)
   for arg in varia:
     print("argumentos de *varia:", arg)


test_var_args('python', 'foo', 'bar', 'pepe')
conjunto=set() #Un conjunto es inmutable y desordenado

#issubset muestra si un conjunto es subconjunto de un conjunto mas grande.
conjunto_a= {1, 2, 3, 4, 5, 6}
conjunto_b= {2, 4}
print(conjunto_a.issubset(conjunto_b)) 
print(conjunto_a.issuperset(conjunto_b))#Super conjunto, el conjunto padre pues
print(conjunto_a.union(conjunto_b))#Los dos conjuntos se unen.
print(conjunto_a.intersection(conjunto_b))#es para encontrar elementos de un conjunto