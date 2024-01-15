'''
Escribir dos funciones, una función que reciba un número entero positivo n 
y calcule el número de fibonacci asociado a ese número, con bucles.

Con ambas funciones, calcular y comparar el tiempo de ejecución para 
n = (1, 10, 20, 30 y 40) por fuerza bruta.
'''

import datetime

def bucle(n):
    '''La función bucle, tiene como parámetro de entrada un número entero, y como salida entregará
    el número de la sucesión de Fibonacci que ocupe esa posición, calculandolo de forma buclica'''
    a = 0
    b = 1
    if n == 0:
        return a 
    if n == 1:
        return b
    if n == 2:
        return a + b
    if n >= 3:
        for i in range(n - 1):
            c = a + b
            a = b
            b = c
        return c
start_time = datetime.datetime.now()
print(bucle(40))
end_time = datetime.datetime.now()

print('El tiempo de ejecución es:', end_time - start_time)

'''
Escribir dos funciones, una función que reciba un número entero positivo n 
y calcule el número de fibonacci asociado a ese número de manera recursiva .

Con ambas funciones, calcular y comparar el tiempo de ejecución para 
n = (1, 10, 20, 30 y 40) por fuerza bruta.
'''

def recursion(n):
    '''La función bucle, tiene como parámetro de entrada un número entero, y como salida entregará
    el número de la sucesión de Fibonacci que ocupe esa posición, calculandolo de manera recursiva'''
    if n <= 1:
        return n
    return recursion(n - 1) + recursion(n - 2)

start_time = datetime.datetime.now()
print(recursion(40))
end_time = datetime.datetime.now()
print('El tiempo de ejecución es:', end_time - start_time)




