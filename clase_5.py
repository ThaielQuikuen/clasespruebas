# if True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo
# else:
#     ... # Bloque de codigo

# if True:
#     ... # Bloque de codigo

# if True:
#     ... # Bloque de codigo
# else:
#     ... # Bloque de codigo

# if True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo

# if True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo

# =============================================================
# =============================================================

# While ( no se conoce cantidad de iteraciones )

# while <condicion>:
#     <bloque de codigo>

# while True:
#     print('Se ejecuto el print')

# while False:
#     print('No salimos mas de aca...')

# ejecucion_nro = 0
# while True:
#     ejecucion_nro += 1
#     print('Se ejecuto el print nro:', ejecucion_nro)

# =============================================================
# =============================================================

# Ejemplo 1

# repetir_menu = True # bandera/flag
# while repetir_menu:
#     print('''
# ==============
#      Menu
# ==============
# 1. Retirar efectivo.
# 2. Cambiar contraseña.
# 3. Salir
# ''')
#     opcion_elegida = input('Ingrese la operacion a realizar: ')
#     if opcion_elegida == '1':
#         print('Retiro efectivo.')
#     elif opcion_elegida == '2':
#         print('Cambio la contraseña.')
#     elif opcion_elegida == '3':
#         print('Hasta luego!')
#         repetir_menu = False
#     else:
#         print('Vuelva a intentar con una opcion valida.')


# =============================================================
# =============================================================

# Ejemplo 2

# numeros = [14, 45, 5, 1234, 1, 4, 9, 15, 25]
# valor_extraido = 0
# while valor_extraido != 5:
#     valor_extraido = numeros.pop()
#     print(valor_extraido)


# =============================================================
# =============================================================

# Ejemplo 3

# hasta = int(input('Ingrese un numero hasta donde quiere sumar'))
# suma = 0
# while hasta:
#     suma += hasta
#     hasta -= 1

# print(f'La suma es {suma}')

# =============================================================
# =============================================================

# Numeros! (10 min)
# Escribir un programa que le pregunte al usuario números hasta que ingrese el 0, 
# cuando lo haga mostrar por pantalla la suma de todos los números ingresados.

# bandera = True
# while bandera:
#     opcion_elegida = input('Ingrese un numero: ')
#     if opcion_elegida == '0':
#         bandera = False

# =============================================================
# =============================================================

# Break

# edad_perro = 1
# while True:
#     print('Guaua!')
#     if edad_perro < 5:
#         edad_perro += 1
#     else:
#         break
#     print('mas valores')
# print('estoy fuera')

# edad_perro = 0
# while edad_perro != 5:
#     print('Guaua!')
#     edad_perro += 1
#     print('mas valores')
# print('estoy fuera')


# =============================================================
# =============================================================

# Continue

# numero = 0
# while numero < 10:
#     numero += 1
#     if numero % 2 == 0:
#         continue
#     print(numero)
    
# print('sali del while')


# =============================================================
# =============================================================

# Pass

# edad_perro = 0
# edad_gato = 0
# if edad_perro == edad_gato:
#     pass # ...
# pass
# print('estoy fuera del if')
# pass


# Usos del pass

# if True:
#     pass # ...

# nombre = input('Ingrese nombre')
# if nombre == '****':
#     pass

# bandera = False
# while bandera:
#     ...

# =============================================================
# =============================================================

# While - Else

# condicion = 10
# while condicion:
#     valor1 = 10
#     suma = valor1 + condicion
#     # if suma == 20:
#     #     break
#     print(f'La suma dio de resultado {suma}')
#     condicion -= 1
# else: # nunca pasa por este bloque de codigo porque se corta el while con el break
#     print('pase por el else')

# variable = 'Aca ya estamos fuera del bucle'
# print(variable)


# =============================================================
# =============================================================

# For ( se conoce cantidad de iteraciones )

# for <variable> in <coleccion>:
#     <bloque de codigo>


# Ejemplo 1

# lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# for dato_de_la_lista in lista:
#     print('Primer print del bucle')
#     print('Dato de la lista', dato_de_la_lista)
#     print('Ultimo print del bucle')

# print('Aca ya estamos fuera del bucle')


# Ejemplo 2

# lista = ['pepe', 9, True, 7, 2.53, 5, 'otro dato', 3, ('soy', 'una', 'tupla'), 1]
# for dato_de_la_lista in lista:
#     print('Primer print del bucle')
#     print('Dato de la lista', dato_de_la_lista)
#     print('Ultimo print del bucle\n')

# print('Aca ya estamos fuera del bucle')


# Ejemplo 3

# lista = [10,9,8,7,6,5,4,3,2,1]
# for dato_de_la_lista in lista:
#     valor1 = 10
#     suma = valor1 + dato_de_la_lista
#     print(f'La suma dio de resultado {suma}')

# print('Aca ya estamos fuera del bucle')


# Ejemplo 4

# indice = 0
# lista = ['pepe', 9, True, 7, 2.53, 5, 'otro dato', 3, ('soy', 'una', 'tupla'), 1]
# for dato_de_la_lista in lista:
#     print(f'Indice: {indice}, valor: {dato_de_la_lista}')
#     indice += 1

# print('Aca ya estamos fuera del bucle')


# Ejemplo 5 ( Ejemplo 3 con modificacion de lista )

# indice = 0
# lista = [10,9,8,7,6,5,4,3,2,1]
# for dato_de_la_lista in lista:
#     valor1 = 10
#     suma = valor1 + dato_de_la_lista
#     print(f'La suma dio de resultado {suma}')
#     lista[indice] = dato_de_la_lista * 2
#     indice += 1

# print(lista)


# =============================================================
# =============================================================

# Desfragmentar tuplas/listas

# Teniendo en cuenta que tenemos una tupla/lista se puede realizar una desfragmentacion
# de la misma para poder guardar cada valor de la misma de forma individual
# como se muestra a continuacion:

# Ejemplo con tupla

# tupla = ('ricado', 4, True)
# nombre, edad, pelado = tupla
# print(tupla)
# print(nombre)
# print(edad)
# print(pelado)

# Ejemplo con lista

# lista = ['ricado', 4, True]
# nombre, edad, pelado = lista
# print(lista)
# print(nombre)
# print(edad)
# print(pelado)


# =============================================================
# =============================================================

# Enumerate

# Devuelve una tupla de tuplas, donde estas ultimas contienen el indice y el valor 
# correspondiente a cada dato de la coleccion


# Ejemplo 1

# lista = [10,9,8,7,6,5,4,3,2,1]
# for valores_devueltos in enumerate(lista):
#     print(valores_devueltos)

# lista = [10,9,8,7,6,5,4,3,2,1]
# for indice, valor in enumerate(lista): # en este caso se usa la desfragmentacion
#     print(indice, valor)


# Ejemplo 2 ( version mejorada del ejemplo 4 del tema For )

# indice = 0
# lista = ['pepe', 9, True, 7, 2.53, 5, 'otro dato', 3, ('soy', 'una', 'tupla'), 1]
# for indice, dato_de_la_lista in enumerate(lista):
#     print(f'Indice: {indice}, valor: {dato_de_la_lista}')

# print('Aca ya estamos fuera del bucle')


# Ejemplo 3 ( version mejorada del ejemplo 5 del tema For )

# lista = [10,9,8,7,6,5,4,3,2,1]
# for indice, valor_de_la_lista in enumerate(lista):
#     valor1 = 10
#     suma = valor1 + valor_de_la_lista
#     print(indice, valor_de_la_lista)
#     print(f'La suma dio de resultado {suma}')
#     # lista[indice] = valor_de_la_lista * 2

# print(lista)


# =============================================================
# =============================================================

# Range

# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for numero in lista:
#     print(numero)

# usando range
# for numero in range(10):
#     print(numero)


# range(<valor final sin incluirlo>)
# for numero in range(10):
#     print(numero)

# range(<valor incial incluido>, <valor final sin incluirlo>)
# for numero in range(4, 10):
#     print(numero)

# range(<valor incial incluido>, <valor final sin incluirlo>, <salto>)
# for numero in range(5, 12, 2):
#     print(numero)

# range pero del numero mas grande al mas chico
# for numero in range(12, 5, -2):
#     print(numero)


# =============================================================
# =============================================================

# # For - For/Else - break/continue/pass
# Para la sentencia for... las funcionalidades de las instrucciones break/continue/pass
# son iguales a las que poseen para la sentencia while, al igual que la sentencia else.

# Descomenta y proba

# for numero in range(5, 15):
#     if numero == 9:
#         break
#     # if numero == 9:
#     #     continue
#     # if numero == 9:
#     #     pass
#     print(numero)
# else:
#     print('pase por el else')


# =============================================================
# =============================================================

# Ejercicio 2 (15 min)

# Haremos el siguiente listado de ejercicios:
# 1. Escribir un programa que enumere los países de la siguiente lista:

# paises = ['Canada', 'USA', 'Mexico', 'Australia', 'Argentina', 'China', 'India']
# for indice, pais in enumerate(paises):
#     print(f'{indice}: {pais}')
    
# 2. Crear un bucle que sume los pares del 0 al 100

# suma = 0
# for numero in range(0, 101, 2):
#     suma += numero
# print(suma)

# 3. Imprimir por pantalla los números del 1 al 10 al revés
# Nota:
# Para imprimir por pantalla al reves se debe usar el mayor número, luego el menor, 
# y el paso sería con -1 range(mayor, menor, -1)

# for numero in range(10, 0, -1):
    # print(numero)

# 4. Pedirle a un usuario que ingrese un número, y devolver los dígitos totales del número
# Por ejemplo, si el número es 75869, la salida debería ser 5.

# numero = input('Ingrese un numero: ')
# print(len(numero))


# =============================================================
# =============================================================

# Revisar Entregable

# =============================================================
# =============================================================