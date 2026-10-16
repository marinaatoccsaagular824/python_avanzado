# Funciones en python

# las funciones nos permite ordenar mejor el codigo y reutilizarlo cuando sea necesario.

# ejemplo deseamos crear un programa en python que nos permita sumar dos numeros
numero_uno:int=45
numero_dos:int=70
numero_tres:int=78
numero_cuatro:int=20
suma:int=numero_uno+numero_dos
suma_dos:int=numero_tres+numero_cuatro
print(suma)
print(suma_dos)

# como hacemos reutilizable el ejercicio anterior y mas lejible.
# para eso utilizaremos funciones.
# la caracteristica de una funcion en python es la siguiente:
# 1. debe comenzar con la palabra reservada def
# 2. debe tener un nombre que de a entender que realizara la funcion.
# 3. debera tener parametros y estos estaran encerrados en parentesistes (). no todas las funciones resibiran parametros aun asi debera tener los ()
# 4. las funciones deberan retornar datos a travez de la palabra reservada return

# crear un programa que me permita sumar dos numeros
def sumar(a:int,b:int):
    return a+b

print (sumar(78,56))
print (sumar(45,5))

# FUNCIONES AVANZADAS
# existen tres grandes conseptos para poder entender el uso avanzado de las funciones:
# 1. argumentos, parametros pocisionales y nominales args y *kargs
# 2. notacones de la salida de una funcion
# 3. recursividad

# anotacion en una funcion
def suma(a:int, b:float) -> int:
    return a + b

# crear unaa funcion que resiva cutro numeros enteros y como salida que me muestre os 4 numeros enters en una lista
def numeros_lista(a:int, b:int, c:int, d:int) -> list[int]:
    return [a, b, c, d]

# crear una funcion que resiva 5 numeros enteros y que retorne solo una listaa de numeros pares, tener en cuenta las anotaciones
def num_pares(a:int,b:int,c:int,d:int,e:int) -> list[int]:
    numeros:list[int]=[a,b,c,d,e]
    numeros_pares:list[int]=[]
    for i in numeros:
        if i%2==0:
            numeros_pares.append(i)
    return numeros_pares

print(num_pares(4,2,6,8,5))  