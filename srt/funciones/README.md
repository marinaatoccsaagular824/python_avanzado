# FUNCIONES DE PYTHON 
las funciones  nos permiten el mejor codigo y utilizarlo cunado sea nesesario.

```python
# ejemplo deseamos crear un programa en python
python que nos permite sumar dos numeros

numero_uno:int=45
numero_dos:int=70
numero_tres:int=78
numero_cuatro:int=20

suma:int=numero_uno+numero_dos
suma_dos:int=numero_tres+numero_cuatro

print(suma)
print(suma_dos)
```
como hacemos reutilizando el ejercicio anterior y mas ligible.
la caracteristica de una funcion en python esla siguente:
1. deve comensar con la palabra reservada `def`
2. deve tener un nombre que de a entender que reali9za la funcion
3. deveria tener parametros y estos estaran enserrados en parentisis ` ()`.no todas las funciones recibiran parametros aun asi deberiann tener los `()`
4. las funciones deberian retornar datos atravez de la palabra reservada `return` 
```python
#crear un programa que me permita sumar dos numeros
def sumar(a:int,b:int):
    return a+b

print(sumar(78,56))
print(sumar(45,5))
 
```