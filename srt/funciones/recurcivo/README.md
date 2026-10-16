## RECURCIVIDAD EN PYTHON
# definicion 
La recursividad en Python es una técnica de programación que consiste en crear una función que se llama a sí misma para resolver un problema. Se utiliza para dividir problemas grandes en partes más pequeñas y fáciles de solucionar. Para que funcione correctamente, debe tener una condición de parada que evite que la función se repita infinitamente.

2.¿Cómo funciona la recursividad?
La recursividad funciona mediante llamadas repetidas de una misma función. Cada llamada realiza una parte del problema hasta llegar a una condición que permite detener el proceso.

Tiene dos elementos principales:

Caso base: es la condición que detiene las llamadas de la función.

Caso recursivo: es la parte del código donde la función se llama a sí misma para continuar resolviendo el problema.

# ejemplo de paython 



Ejemplo de recursividad en Python
El siguiente programa calcula el factorial de un número utilizando una función recursiva.


```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
```