"""
Importamos los modulos timeit y tracemalloc para ver cuanta memoria y tiempo tarda el programa
en ejecutarlo asi puedes hacer un analisis empirico
"""

from timeit import timeit
import tracemalloc
"""
En la entrada de este algoritmo tienes que poner el numero entero que quieras que encuentre sus
numeros primos precedentes
"""
n=int(input("numeros antes de este que sean primos: "))

"""
Este algoritmo utiliza Programacion Dinamica para que sea más optimo.
Utilizando el metodo de Bottom-up. En otras palabras, creamos una tabla y vamos recoriendo
la lista viendo si es primo o no.
Este algorimo identifica:
1: como no primo (FALSE)
0: como ser primo (TRUE)
Finalmente devuelve la lista de los indices qe tengan 0 (los primos).
"""
def CribaEratóstenes(n):
    # Crear tabla de n de largo
    Prime_table = [0] * (n+1) 
    # Sabemos que 0 y 1 no son primos segun la definición de primo
    Prime_table[0]=Prime_table[1]=1
    
    for i in range(2, n+1):  # Iterar por todos los números desde 2 hasta n

        if Prime_table[i] == 0:  # comprobar si es primo
            """
            Si es primo entonces recoremos la lista.
            Poniendo No primos a los numeros que sean
            multiplos de el numeros primo.
            Esto lo hacemos multiplicandolo por 2 de i en i
            Hasta que terminamos la lista
            """
        
            for j in range(2 * i, n+1,i): 
                Prime_table[j] = 1 # Marcar los multiplos de las i no primos
    """
    Alfinal todos los multiplos de las siguientes i estaran marcadas como 1 dejando solo 
    los primos que luego haremos una lista que coje los indices de todos los que tengan un 0
    """
    lista=[i for i in range(2, n+1 ) if Prime_table[i] == 0]# Check prima ver crear lista de indices

    return lista

tracemalloc.start()

sal=CribaEratóstenes(n)# lista de numeros primos

Tiempo_CribaEratóstenes=timeit(lambda:CribaEratóstenes(n),number=10)# mira el tiempo

current, peak = tracemalloc.get_traced_memory()# la memoria utilizada

tracemalloc.stop()

bel=len(sal) # cuantos numeros primos hay precedentes

"""
El output de este algoritmo sera una lista de los numeros primos.
Con cuantos numeros primos hay en la lista cuanto a tardado y la memoria utilizada
"""

print("Numeros primos precedentes:\n",sal)
print("numeros de primos anteriores\n",bel)
print("Tiempo de buscar primos precedentes es: \n",Tiempo_CribaEratóstenes," segundos")
print(f"Memoria de primos precedentes {current/10**6} MB y un pico en {peak/10**6} MB")
