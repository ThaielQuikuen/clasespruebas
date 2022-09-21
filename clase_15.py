# Scripts, Modulos y Paquetes

# print('Mi primer script')

# valor1 = 'pepe'
# print(valor1)

# print(input('Dame un valor a mostrar: '))

# Pasar argumentos

# import sys

# print(sys.argv)
# print(type(sys.argv))
# lista_de_argumentos = sys.argv[1:]


# Ejercicio Aprobemos
# Crear un script llamado aprobado.py que realice lo siguiente:

# Debe tomar 2 argumentos, ambos números enteros del 0 al 10, sino, mostrar un error.
# Si ambos valores son mayores o igual a 7 imprimir “Promocionado”
# Si ambos valores son mayor o igual a 4 imprimir “Aprobado, debe rendir final”

# Si uno de los dos valores es menor a 4 imprimir 
# “Desaprobado, debe recuperar el primer parcial” 
# (Si el primer argumento es 3 debe recuperar el primer parcial, 
# si no, debe decir lo mismo pero con segundo parcial)

# Si ambos argumentos son menores a 4 debe imprimir “Desaprobó ambos parciales, debe recursar”
# En caso de no mostrar uno o ambos argumentos debe mostrar información de como usar el script.

# import sys

# if len(sys.argv[1:]) >= 2:

#     valor1 = int(sys.argv[1])
#     valor2 = int(sys.argv[2])

#     if (
#         valor1 in range(11) and
#         valor2 in range(11)
#     ):
#         if (
#             valor1 >= 7 and
#             valor2 >= 7
#         ):
#             print('Promocionado')
#         elif (
#             valor1 >= 4 and
#             valor2 >= 4
#         ):
#             print('Aprobado, debe rendir final')
#         elif (
#             valor1 == 3
#         ):
#             print('Desaprobado, debe recuperar el primer parcial')
#         elif (
#             valor1 < 4 or
#             valor2 < 4
#         ):
#             print('Desaprobado, debe recuperar el segundo parcial')
#         elif (
#             valor1 < 4 and
#             valor2 < 4
#         ):
#             print('Desaprobó ambos parciales, debe recursar')  

# Modulos

# Crear archivo de funciones, diferentes formas de invocar

# import modulo
# from modulo import algo, otra_cosa
# from modulo import algo as algo_llamado_distinto, otra_cosa
# from modulo import *

# v1
# import mis_funcionalidades

# print(mis_funcionalidades.sumar(5, 4))

# persona1 = mis_funcionalidades.Persona('Ricardo')
# print(persona1.nombre)

# v2
# from mis_funcionalidades import sumar, Persona

# print(sumar(5, 4))

# persona1 = Persona('Ricardo')
# print(persona1.nombre)

# v3
# from mis_funcionalidades import *

# print(sumar(5, 4))

# persona1 = Persona('Ricardo')
# print(persona1.nombre)


# v4
# from mis_funcionalidades import *

# sumar = 5

# print(sumar(5, 4))

# persona1 = Persona('Ricardo')
# print(persona1.nombre)

# v5
# from mis_funcionalidades import sumar as sumar_de_mi_modulo, Persona

# sumar = 5

# print(sumar_de_mi_modulo(5, 4))

# persona1 = Persona('Ricardo')
# print(persona1.nombre)


# Ej Primer Modulo (10min)
# Hacer una clase fácil, como Persona, con nombre y apellido, con un método hablar()
# Crear una instancia de persona, mostrando sus datos y llamando al método desde otro módulo.


# Comentar la variable __name__

# print(__name__)

# Paquetes
 
# Crear un paquete con sus modulos

# from matematicas.resta import restar

# print(restar(5, 3))


# Paquetes redistribuibles

# collections

# from collections import namedtuple, Counter

# Pescado = namedtuple('Pescado', ['nombre', 'especie', 'peso'])

# pescado1 = Pescado('pecesin', 'payaso', 200)

# print(Pescado)
# print(pescado1)
# print(pescado1.nombre)
# print(pescado1[0])
# print(pescado1._asdict())
# print(list(pescado1._asdict().items())[0])

# print(Counter('abcabc123'))
# print(Counter((1,2,3,4,5,3,5,7,8,9,1,1,1,2,2)))

# datetime

# from datetime import datetime, timedelta

# dt = datetime.now()
# print(dt)

# dt_custom = datetime(2000, 1, 1)
# print(dt_custom)

# print(dt.strftime("%A %d %B %Y %I:%M"))
# print(dt.hour)

# dt1 = dt.replace(day=5)
# print(dt)
# print(dt1)

# td = timedelta(days=15)

# dato_de_fecha_modificado = dt + td
# dato_de_fecha_modificado = dt - td
# print(dato_de_fecha_modificado)


# Ejercicio 3
# Calcular tu edad con la mayor precisión posible. Utilizando un módulo llamado fechas.py.
# ¿Cuántos segundos faltan para tu cumpleaños?



# math

# import math

# print(math.pi)
# print(math.sqrt(64))
# print(round(3.3))
# print(round(3.5))
# print(round(3.8))
# print(math.floor(3.8))
# print(math.ceil(3.3))

import random

# print(random.randrange(15))
# print(random.randrange(15, 22))
# print(random.randrange(15, 22, 2))

lista = ['hoy', 'corri', '4', 'kilometros']
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choice(lista))
print(random.choices(lista, k=3))
# print(random.choices(lista, k=3))
# print(random.choices(lista, k=3))
# print(random.choices(lista))




