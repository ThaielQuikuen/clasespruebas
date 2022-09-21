# open, close (w, r, a)

# https://docs.python.org/3/library/functions.html#open

# archivo_abierto = open('texto.txt', 'w')
# print(type(archivo_abierto))

# # Trabajamos con el archivo
# #  y al finalizar lo debemos cerrar

# archivo_abierto.close()


# with open('texto.txt', 'w') as archivo_abierto:
#     # Trabajamos con el archivo
# # Una vez fuera del with el archivo se cierra solo


# write

# archivo_abierto = open('archivos_clase8/texto.txt', 'w')
# archivo_abierto = open('archivos_clase8/texto123.txt', 'a')
# archivo_abierto = open('archivos_clase8/texto123.txt', 'w')

# archivo_abierto.write('Esto es una prueba\n')
# archivo_abierto.write('Soy otra cosa')
# archivo_abierto.write('Pise el texto')

# archivo_abierto.close()


# archivo_abierto = open('archivos_clase8/texto123.txt', 'w')

# archivo_abierto.write('Pepe')

# archivo_abierto.close()

# read, readline, readlines
# archivo_abierto = open(r'datos.txt', 'r', encoding="utf-8")
# archivo_abierto = open(r'..\datos.txt', 'r')
# archivo_abierto = open(r'C:\Source Code\Coder\41765\datos.txt', 'r')
# print(type(archivo_abierto))

# print(archivo_abierto.read())
# print('----------------')
# print(archivo_abierto.read())
# print('----------------')

# print(archivo_abierto.readline())
# print(archivo_abierto.readline())
# print(archivo_abierto.readline())

# print(archivo_abierto.readlines())
# print(archivo_abierto.readlines())
# print(len(archivo_abierto.readlines()))

# archivo_abierto.close()

# archivo_abierto = open(r'datos.txt', 'r', encoding="utf-8")

# texto = archivo_abierto.read()

# print(archivo_abierto.read())
# archivo_abierto.close()

# print('----------------')
# print('----------------')
# print(texto)
# print('----------------')
# print('----------------')
# print(texto)


# seek

# archivo_abierto = open(r'datos.txt', 'r', encoding="utf-8")
# archivo_abierto = open(r'datos.txt', 'w', encoding="utf-8")
# archivo_abierto = open(r'datos.txt', 'a', encoding="utf-8")

# print(archivo_abierto.read())
# archivo_abierto.seek(1)
# print('----------------')
# print(archivo_abierto.read())

# print(archivo_abierto.readline())
# archivo_abierto.seek(2)
# print('----------------')
# print(archivo_abierto.readline())

# lineas = archivo_abierto.readlines()
# print(archivo_abierto.readlines())

# archivo_abierto.seek(25)

# print(archivo_abierto.readlines())


# archivo_abierto.close()

# nuevas_lineas = []
# for linea in lineas:
#     nuevas_lineas.append(linea.upper())
    
# print(nuevas_lineas)

# archivo_abierto = open(r'datos.txt', 'w', encoding="utf-8")
# archivo.write(''.join(nuevas_lineas))
# archivo_abierto.write(nuevas_lineas[2])
# archivo_abierto.close()

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }

# with open('archivos_clase8/datos_auto.txt', 'w') as archivo:
#     archivo.write(f'{auto["motor"]}\n')
#     archivo.write(f'{auto["color"]}\n')
#     archivo.write(f'{auto["vidrios"]}\n')
#     archivo.write(f'{auto["pasajeros"]}\n')
#     archivo.write(f'{auto.get("Ricardo", "otro valor")}\n')

# with open('archivos_clase8/datos_auto.txt', 'w') as archivo:
#     archivo.write('''
# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# ''')
    
# json

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }

# lista = [1,2,3,4,5,6,7]

# import json

# # dump
# with open('archivos_clase8/mi_archivo.json', 'w') as archivo_para_guardar:
#     json.dump(auto, archivo_para_guardar, indent=4)
#     # json.dump(lista, archivo_para_guardar, indent=4)

# # load
# with open('archivos_clase8/mi_archivo.json', 'r') as archivo_para_leer:
#     datos = json.load(archivo_para_leer)
#     print(datos)
#     print(type(datos))


# import pandas as pd

# datos = pd.read_csv(r'dataset_viajes_sube.csv')
# print(datos)
# NOT A NUMBER (NaN) => null, None

# print(datos.head())
# print(datos.head(10))

# print(datos.tail())
# print(datos.tail(3))

# print(datos.sample(3))

# print(datos)
# print(datos['TIPO_TRANSPORTE'])
# print(datos['TIPO_TRANSPORTE'].value_counts())