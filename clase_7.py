# -*- coding: utf-8 -*-
"""
Clase 7 - Metodos de colecciones


# Strings

Método upper
"""

# cadena1 = 'soY la pRimer cadena'
# print(cadena1)
# cadena1_en_mayusculas = cadena1.upper()
# # cadena1 = cadena1.upper()
# print(cadena1)
# print(cadena1_en_mayusculas)

"""
Método lower
"""

# cadena1 = 'soY la pRimer cadena'
# cadena1_en_minusculas = cadena1.lower()
# print(cadena1)
# print(cadena1_en_minusculas)

"""
Método capitalize
"""

# cadena1 = 'soY la pRimer cadena'
# cadena1_capitaliciada = cadena1.capitalize()
# print(cadena1)
# print(cadena1_capitaliciada)

"""
Método title
"""

# cadena1 = 'soY la pRimer cadena'
# cadena1_titleada = cadena1.title()
# print(cadena1)
# print(cadena1_titleada)

"""
Método count
"""

# cadena1 = 'soY la pRimer cadena'
# cadena1 = 'soY la pRimeroY cadenaoY  oY'
# print(cadena1.count('oy'))
# print(cadena1.count('oY'))
# print(cadena1.count('a'))
# print(cadena1.count('a', 2))
# print(cadena1.count('a', 7))
# print(cadena1.count('a', 2, 16))

"""
Método find
->
"""

# cadena1 = 'soY la pRimer oY cadena'
# print(cadena1.find('oy'))
# print(cadena1.find('oY'))
# print(cadena1.find('oY', 2, 17))
# print(cadena1.find('oY', 2, 14))
# print(cadena1.find('oY', 2, 15))

"""
Método rfind
<-
"""

# cadena1 = 'soY la pRimer oY cadena'
# print(cadena1.rfind('oy'))
# print(cadena1.rfind('oY'))
# print(cadena1.rfind('oY', 1, 4))

"""
Método split y join
"""

# cadena2 = 'segunda cadena al rescate'
# # cadena2_spliteada = cadena2.split()
# # cadena2_spliteada = cadena2.split('a')
# cadena2_spliteada = cadena2.split('ca')
# # cadena2_spliteada = cadena2.split('q')
# # cadena2_spliteada = list(cadena2)
# print(cadena2)
# print(cadena2_spliteada)

# print('co'.join(cadena2_spliteada))
# # print(' '.join(cadena2_spliteada))
# print(''.join(cadena2_spliteada))

# lista = ['11','12','13','14','15','16','17']
# conjunto = {'11','12','13','14','15','16','17'}
# print(' <-> '.join(lista))
# print(' <-> '.join(conjunto))

# palabra = 'pepe'
# # print('123'.join(palabra))
# # print('123'.join(1))
# print('123'.join([palabra]))

"""
Método strip
"""

# password = input('Ingrese un password: ')
# print(password.strip())
# print(password)


# print(password.strip('tor'))
# password.strip()
# print(password)
# print('..dsapepea.sd'.strip('asd.'))

"""
Método replace
"""

# palabra_repetida = 'cadena cadena cadena cadena cadena'
# palabra_repetida_modificada = palabra_repetida.replace('cadena', 'otra')
# print(palabra_repetida)
# print(palabra_repetida_modificada)
# print(palabra_repetida.replace('cadena', 'otra', 3))

"""
# Listas

Método clear
"""

# lista1 = ['primera', 'lista', 1]
# lista2 = ['segunda', 'lista', 2]
# lista1 = []
# lista2.clear()
# print(lista1)
# print(lista2)

"""
Método extend
"""

# lista1 = ['primera', 'lista', 1]
# lista2 = ['segunda', 'lista', 2]
# # # lista1 += lista2
# # # print(lista1)
# lista1.extend(lista2)
# # lista1.extend('otro')
# print(lista1)

"""
Método insert
"""

# lista2 = ['segunda', 'lista', 2]
# dicc = {
#     'llave': 'valor'
# }
# print(lista2)
# lista2.insert(1, dicc)
# print(lista2)

"""
Método reverse
"""

# lista2 = ['segunda', 'lista', 2]
# print(lista2)
# # lista2 = lista2[::-1]
# lista2.reverse()
# print(lista2)

"""
Método sort
"""

# lista_numeros = [5,1,2,3,4,10]
# # lista_numeros.sort()
# lista_numeros.sort(reverse=True)
# print(lista_numeros)


# # lista_numeros1 = ['5','1','2','3','4','10']
# lista_numeros1 = ['pepe','hola','eras']
# lista_numeros1.sort()
# # lista_numeros1.sort(reverse=True)
# print(lista_numeros1)

"""
Ejercicio - colecciones 1 (20min)


Utilizando todo lo que sabes sobre cadenas, listas y
sus métodos internos, transforma este texto:

texto = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista'

En este:

Gordon lanzó su curva...
- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
- Dos pies -le corrigió Troop.
- Strawberry menea la cabeza como disgustado… -agrega el comentarista.

"""

texto = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista'

# lista = texto.split('&')
# lista[0] += '..'
# lista2 = []
# for oracion in lista:
#     lista2.append(oracion[0].upper() + oracion[1:])

# texto2 = '.\n- '.join(lista2)
# texto2 += '.'

# print(texto2)

"""
# break

# Conjuntos
"""

# numero1 = 1
# numero2 = numero1
# numero1 += 2
# print(numero1)
# print(numero2)

# conjunto1 = {1, 'conjunto1', (1, True)}
# conjunto3 = conjunto1
# print(conjunto3)
# conjunto1.add(456)
# print(conjunto3)


# posiciones en disco |15|25|14|10|  |
#                     |  |  |  |  |  |  

# guarda {1, 'conjunto1', (1, True)} en la posicion 15 de disco
# conjunto1 <--- posicion del disco 15

"""
### Copy
"""

# conjunto1 = {1, 'conjunto1', (1, True)}
# # conjunto3 = conjunto1
# conjunto3 = conjunto1.copy()
# print(conjunto3)
# conjunto1.add(456)
# print(conjunto3)

# # # listas o tuplas -->> lista2 = lista[:] / tupla2 = tupla[:]
# lista1 = [1,2,3,4,5]
# lista2 = lista1
# # lista2 = lista1[:]
# print(lista2)
# lista1.append(45)
# print(lista2)

"""
Método isdisjoint (distintos)
"""

# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = [1, 'valor1', (1, True)]
# # el primero tiene que ser un set... el segundo un iterable
# # print(conjunto1.isdisjoint(iterable1))

# iterable2 = (2, 'valor2', (2, True))
# print(conjunto1.isdisjoint(iterable2))

"""
Método issubset
"""

# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (1, 'valor1', (1, True), 45)
# print(conjunto1.issubset(iterable1))


# iterable2 = (1, 'valor1', (1, True))
# print(conjunto1.issubset(iterable2))


# iterable3 = (2, 'valor1', (1, True))
# print(conjunto1.issubset(iterable3))

"""
Método issuperset
"""

# conjunto1 = {1, 'valor1', (1, True), 45}
# iterable1 = (1, 'valor1', (1, True), 45)
# print(conjunto1.issuperset(iterable1))


# iterable2 = (1, 'valor1', (1, True))
# print(conjunto1.issuperset(iterable2))


# iterable3 = (2, 'valor1', (1, True))
# print(conjunto1.issuperset(iterable3))

"""
Método union
"""

# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (2, 'valor2', (2, True), 45)
# conjunto3 = conjunto1.union(iterable1)
# print(conjunto1)
# print(conjunto3)

"""
Método difference
"""

# conjunto1 = {1, 'valor1', (1, True)}
# # iterable1 = (2, 'valor2', (2, True), 45)
# iterable1 = (2, 'valor2', (1, True), 45)
# print(conjunto1.difference(iterable1))
# print(conjunto1)

"""
Método difference_update
"""

# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (1, 'valor2', (1, True), 45)
# conjunto1.difference_update(iterable1)
# print(conjunto1)

"""
Método intersection
"""

# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (1, 'valor2', (1, True), 45)
# print(conjunto1.intersection(iterable1))
# print(conjunto1)

"""
Método intersection_update
"""

# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (1, 'valor2', (1, True), 45)
# conjunto1.intersection_update(iterable1)
# print(conjunto1)

"""
# Diccionarios

Método get
"""

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# valor1 = auto['motor']
# print(valor1)
# # valor2 = auto['ricardo']
# # print(valor2)
# valor3 = auto.get('ricardo', False)
# print(valor3)

"""
Método keys
"""

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# print(auto.keys())
# print(list(auto.keys()))
# for llave in auto.keys():
#     print(llave)

"""
Método values
"""

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# print(auto.values())
# print(list(auto.values()))
# for valor in auto.values():
#     print(valor)
# print(type(auto.values()))

"""
Método items
"""

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# print(auto.items())
# print(list(auto.items()))
# for llave, valor in auto.items():
#     print(f'Para la llave {llave} el valor es {valor}')

"""
### Ejercicio - colecciones 2 (30min)

A partir de una lista realizar las siguientes tareas sin modificar la lista original:
1. Borrar los elementos duplicados
2. Ordenar la lista de mayor a menor
3. Eliminar todos los números impares
4. Realizar una suma de todos los números que quedan
5. Añadir como primer elemento de la lista la suma realizada
6. Devolver la lista modificada
7. Finalmente, después de ejecutar la función, comprueba que la suma de todos 
los números a partir del segundo, concuerda con el primer número de la lista

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
"""

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

# 1. Borrar los elementos duplicados
lista_nueva = list(set(lista))

# 2. Ordenar la lista de mayor a menor
lista_nueva.sort(reverse=True)

# 3. Eliminar todos los números impares
lista_final = []
for numero in lista_nueva:
    if numero%2==0:
        lista_final.append(numero)

# 4. Realizar una suma de todos los números que quedan
suma = sum(lista_final)

# 5. Añadir como primer elemento de la lista la suma realizada
lista_final.insert(0, suma)

# 6. Devolver la lista modificada
print(lista_final)

# 7. Finalmente, después de ejecutar la función, comprueba que la suma de todos 
# los números a partir del segundo, concuerda con el primer número de la lista
print(f'El valor {lista_final[0]} es igual a {sum(lista_final[1:])} que es la suma de lops valores {lista_final[1:0]}')