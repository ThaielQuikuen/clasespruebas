"""
# Set ( heterogeneos )
"""

# lista = ['soy', 'una', 'lista', 2, True]
# tupla = ('soy', 'una', 'tupla', 2, True)
# conjunto = {'soy', 'un', 'conjunto', 1, True}

"""# Set vacio"""

# otros_datos = []
# otros_datos1 = ()
# otros_datos2 = {}
# otros_datos3 = set()
# print(type(otros_datos))
# print(type(otros_datos1))
# print(type(otros_datos2))
# print(type(otros_datos3))

"""# Asignacion en un set"""

# lista = ['soy', 'una', 'lista', 2, True]
# tupla = ('soy', 'una', 'tupla', 2, True)
# conjunto = {'soy', 'un', 'conjunto', 1, False, 0}

# print(lista[1])
# print(tupla[1])
# print(conjunto[1])
# print(conjunto)
# print(conjunto)

# lista[1] = 'uno'
# print(lista)
# tupla[1] = 'uno'
# print(tupla)
# conjunto[1] = 'uno'
# print(conjunto)

"""# Objetos mutables y los sets"""

# prueba = {1, 2, 3, 'hola', 'como', 'estas'}
# otra_prueba1 = [(1,2,3), [6,7,8]]
# otra_prueba2 = ((1,2,3), [6,7,8])
# otra_prueba3 = {(1,2,3), [6,7,8]}
# print(otra_prueba1)
# print(otra_prueba2)
# print(otra_prueba3)

# otra_prueba1[1][2] = 5
# print(otra_prueba1)
# otra_prueba2[1][2] = 5
# print(otra_prueba2)
# otra_prueba2[1] = 5
# print(otra_prueba2)

"""# Set generado con iterables"""

# lista_prueba = [1, 2, 3, 'hola', 'como', 'estas', ['otra', 'lista']]
# lista_prueba = [1, 2, 3, 'hola', 'como', 'estas', ('otra', 'lista')]
# conjunto_prueba = set(lista_prueba)
# tupla_prueba = (1, 2, 3, 'hola', 'como', 'estas')
# conjunto_prueba = set(tupla_prueba)
# print(conjunto_prueba)
# conjunto_prueba2 = set(range(10))
# print(conjunto_prueba2)
# print(type(lista_prueba))
# print(type(conjunto_prueba))
# print(type(conjunto_prueba2))

"""# No se repiten valores"""

# lista = [1,2,3,4,5,6,6,6,6,1,2,3]
# conjunto = {1,2,3,4,5,6,6,6,6,1,2,3}
# print(lista)
# print(conjunto)
# print(set(lista))

"""============================================================
============================================================
# Funciones Integradas
============================================================
============================================================
"""

# auto = {'v8', 'Negro', (6, 'blindadas')}
# # print(auto)

# """# Método add"""

# # lista = [1, 2, 3, 'probando']
# tupla = (1, 2, 3, 'probando')
# auto.add('descapotable')
# # auto.add(lista)
# auto.add(tupla)
# print(auto)

"""# Método update"""

# auto = {'v8', 'Negro', (6, 'blindadas')}
# lista = ['soy', 'una', 'lista']
# tupla = ('soy', 'una', 'tupla')
# cadena = 'soy una cadena'
# rango = range(15)
# auto.update(lista)
# auto.add('soy')
# auto.add('una')
# auto.add('lista')
# print(auto)
# auto.update(tupla)
# print(auto)
# auto.add(cadena)
# auto.update(cadena)
# print(auto)
# auto.update(rango)
# print(auto)

# auto = {'v8', 'Negro', (6, 'blindadas')}
# auto.add(range(15))
# print(auto)


"""# Función len"""

# auto = {'v8', 'Negro', (6, 'blindadas')}
# print(len(auto))

"""# Método discard"""

# auto = {'v8', 'Negro', (6, 'blindadas')}
# auto.discard('lista')
# print(auto)
# auto.add('lista')
# print(auto)
# auto.discard('lista')
# print(auto)

"""# Método remove ( discard pero con generacion de error )"""

# auto = {'v8', 'Negro', (6, 'blindadas')}
# auto.remove('tupla')
# print(auto)
# auto.add('tupla')
# print(auto)
# auto.discard('tupla')
# print(auto)

"""# Operador in"""

# auto = {'v8', 'Negro', (6, 'blindadas')}
# # for dato in auto:
# #     print(dato)
# print('descapotable' in auto)
# print('caño de escape' not in auto)
# lista = [1,2,3,4]
# print(1 in lista)

"""# Método clear"""

# auto = {'v8', 'Negro', (6, 'blindadas')}
# print(auto)
# auto = set()
# # auto.clear()
# print(auto)

"""# Método pop"""

# auto = {'v8', 'Negro', (6, 'blindadas')}
# print(auto)
# valor = auto.pop()
# print(auto)
# print(valor)

# while len(auto): 
#     print(auto)
#     valor = auto.pop()
#     print(valor)

"""# Ej Sets (10min)
Programa las siguientes instrucciones de forma ordenada sobre la variable grupo:
1. Añade los usuarios: Ana, Ramón, Marta, Eric, David
2. Elimina los usuarios: Mario, Miguel, Esteban

grupo = {'Miguel', 'Blanca', 'Mario', 'Andrés'}
"""

# grupo = {'Miguel', 'Blanca', 'Mario', 'Andrés'}

# # v2
# # grupo.add("Ana")
# # grupo.add("Ramón")
# # grupo.add("Marta")
# # grupo.add("Eric")
# # grupo.add("David")

# # v1
# agregar = ("Ana", "Ramón", "Marta", "Eric", "David")
# grupo.update(agregar)

# grupo.discard("Mario")
# grupo.discard("Miguel")
# # grupo.remove("Esteban")
# # grupo.discard("Esteban")
# print(grupo)



"""# BREAK

# Diccionarios
"""

dicc = {}

"""Las claves/llaves/keys pueden ser cualquier valor inmutable

los valores/values pueden ser cualquier valor posible


```

dicc = { clave: valor, clave2: valor2, clave3: valor3, ...}

dicc1 = {
    clave: valor,
    clave2: valor2,
    clave3: valor3,
    ...
}

dicc2 = {
    clave: dicc1,
    clave2: valor2,
    clave3: valor3,
    ...
}

dicc3 = {
    0: ['soy', 'una', 'lista'],
    'string': ('soy', 'una', 'tupla'),
    ('tupla', 'llave'): 'la tupla es mi llave'
}
```
"""

# auto = {'v8', 'Negro', (6, 'blindadas')}
# # print(auto)
# motor = 'v8'
# color = 'Negro'

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4
# }
# print(auto)

"""
# Acceso, mutabilidad, asignación, agregado de valores"""

# lista = ['soy', 'una', 'lista']
# print(lista[1])
# lista[1] = 24
# print(lista)
# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
#     4: 'el valor de la clave 4'
# }
# print(auto['motor'])
# print(auto['canio de escape'])
# print(auto.get('motor'))
# print(auto.get('canio de escape'))
# print(type(None))
# print(auto.get('canio de escape', 45))
# print(auto.get('canio de escape', input('que valor por defecto queres: ')))

# print(auto)
# auto['motor'] = 'v12'
# print(auto['motor'])
# print(auto)
# print(auto[4])
# auto['modelo'] = 2016
# print(auto)
# auto['pasajeros'] += 1
# print(auto)

"""============================================================
============================================================
# Funciones Diccionarios
============================================================
============================================================

# Método update
"""

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# pepe = (1, 2)
# auto.update({pepe: 'valor1', 'llave2': 'valor2', 'motor': 'v12'})
# print(auto)
# print(auto[(1, 2)])
# auto.update((('llave1', 'valor1'), ('llave2', 'valor2'), ('motor', 'v12')))
# print(auto)

"""
# Función len"""

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# print(len(auto))

"""
# Función del"""

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# del auto['color']
# # del auto['ricardo']
# print(auto)

"""
# Operador in"""

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# print('motor' in auto)
# print('v8' in auto)
# print('v12' not in auto)

"""
# Método clear"""

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# # auto.clear()
# auto = {}
# print(auto)

"""
# Método pop"""

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }

# print(auto)
# valor = auto.pop()
# print(auto)
# print(valor)


# print(auto)
# valor = auto.pop('pasajeros')
# print(auto)
# print(valor)


# print(auto)
# valor = auto.pop('ricardo')
# print(auto)
# print(valor)


# print(auto)
# valor = auto.pop('ricardo', 'este valor sale por defecto si no se encuentra la llave buscada')
# print(auto)
# print(valor)



# valor = auto.pop('ricardo', input('dame un dato'))
# valor = auto.pop('color', 'la llave color no se encontro')
# valor = auto.pop(input('dame la key...?'), [1,2,3,45])
# print(auto)
# print(valor)

"""# Ej Dics (10min)
Programa las siguientes instrucciones de forma ordenada sobre la variable animales:
1. Inicialmente el diccionario es: animales = {"elefante": ""}
2. Añade al diccionario las claves perro, tigre y mono con sus respectivos valores Bobby, Pepe y Homero
3. Modificá las claves elefante y delfin con los valores Trompis y Manolo respectivamente
"""

# animales = {"elefante": ""}

# animales_a_agregar = {'perro': 'Bobby', 'tigre': 'Pepe', 'mono': 'Homero'}
# animales.update(animales_a_agregar)

# animales['elefante'] = 'Trompis'
# animales['delfin'] = 'Manolo'

# print(animales)