# https://www.seas.es/blog/informatica/agregacion-vs-composicion-en-diagramas-de-clases-uml/
# Slides

# Definiendo e instanciar una clase
'''
class Auto:
    ... # pass
    
auto1 = Auto()
auto2 = Auto()
'''

# def funcion():
#     return 'valor'

# valor = funcion()
# print(valor)


# class ClaseAuto: # PascalCase
#     ...

# auto1 = ClaseAuto()
# auto2 = ClaseAuto()

# # print(type(2))
# # print(type(auto1))
# # print(type(auto2))

# # print(funcion)
# # print(ClaseAuto)
# print(auto1)
# print(auto2)


# Base sobre metodos

# class ClaseAuto: # PascalCase
            
#     def tocar_bocina(self):
#         print('Pi pi!!')  

#     def describir_auto(self):
#         return f'Este es un auto.'


# auto1 = ClaseAuto()
# auto2 = ClaseAuto()

# auto1.tocar_bocina()
# print(auto1.describir_auto())

# auto2.tocar_bocina()
# print(auto2.describir_auto())


# Atributos

# De instancia
'''
class Auto:
    
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca
'''

# class FordK:
    
#     def __init__(self, color, puertas):
#         self.color = color
#         self.puertas = puertas

# # auto1 = FordK()
# # auto2 = FordK()
# auto1 = FordK('Negro', 4)
# auto2 = FordK('Rojo', 2)
# auto3 = FordK('Rojo', 3)

# print(auto1)
# print(f'Color de auto1 {auto1.color}')
# print(f'Cant puertas {auto1.puertas}')
# print(auto2)
# print(f'Color de auto2 {auto2.color}')
# print(f'Cant puertas {auto2.puertas}')


# class FordK:
    
#     def __init__(self, color, puertas):
#         self.color = color
#         self.puertas = puertas
        
#     def tocar_bocina(self):
#         print('Pi pi!!')
    
#     def describir_auto(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'
    

# # auto1 = FordK.__init__('Negro', 4)
# auto1 = FordK('Negro', 4)
# auto2 = FordK('Rojo', 2)

# # print(auto1)
# # print(f'Color {auto1.color}')
# # print(f'Cant puertas {auto1.puertas}')
# # auto1.tocar_bocina()
# print(auto1.describir_auto())

# # print(auto2)
# # print(f'Color {auto2.color}')
# # print(f'Cant puertas {auto2.puertas}')
# # auto2.tocar_bocina()
# print(auto2.describir_auto())

# ======================================================
# ======================================================

# Valores por defecto

# class FordK:
    
#     def __init__(self, color='Verde', puertas=5):
#         self.color = color
#         self.puertas = puertas
        
#     def tocar_bocina(self):
#         print('Pi pi!!')
    
#     def describir_auto(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'
    

# auto1 = FordK('Negro', 4)
# auto2 = FordK('Rojo', 2)
# auto3 = FordK(puertas=2)
# auto4 = FordK('Rojo')
# auto5 = FordK()

# print(auto1.color, auto1.puertas)
# print(auto2.color, auto2.puertas)
# print(auto3.color, auto3.puertas)
# print(auto4.color, auto4.puertas)
# print(auto5.color, auto5.puertas)

# *args, **kwargs en constructor


# print(type(auto1))
# print(type(auto2))

# ======================================================
# ======================================================

# Atributo de clase

# class FordK:
  
#     cant_ruedas = 4
    
#     def __init__(self, color='Verde', puertas=5):
#         self.color = color
#         self.puertas = puertas
#         self.radio = True
        
#     def tocar_bocina(self):
#         print('Pi pi!!')
    
#     def describir_auto(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'


# auto1 = FordK('Negro', 4)
# auto2 = FordK('Rojo', 2)
# auto3 = FordK(puertas=2)
# auto4 = FordK('Rojo')
# auto5 = FordK()

# print(auto1.color, auto1.puertas, auto1.cant_ruedas)
# print(auto2.color, auto2.puertas, auto2.cant_ruedas)
# print(auto3.color, auto3.puertas, auto3.cant_ruedas)
# print(auto4.color, auto4.puertas, auto4.cant_ruedas)
# print(auto5.color, auto5.puertas, auto5.cant_ruedas)

# print(type(auto1))
# print(type(auto2))

# print(FordK.cant_ruedas)
# print(FordK.color)

# ======================================================
# ======================================================

# Metodos

# class FordK:
  
#     cant_ruedas = 4
    
#     def __init__(self, color='Verde', puertas=5):
#         self.color = color
#         self.puertas = puertas
#         self.metros_recorridos = 0
#         self.fabricar()
    
#     def tocar_bocina():
#         print('Pi pi!!')
#         # self.toco_bocina = True
    
#     # def __str__(self):
#     #     return self.describir_auto()
    
#     def describir_auto(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'

#     def fabricar(self):
#         print(f'Se fabrico un Ford K {self.color} de {self.puertas} puertas.')
        
#     def avanzar(self, metros):
#         print(f'el auto avanzo {metros} metros')
#         self.metros_recorridos += metros


# auto1 = FordK('Negro', 4)
# print(auto1)
# print(auto1.toco_bocina)
# auto1.tocar_bocina()
# print(auto1.describir_auto())
# print(auto1.toco_bocina)
# auto1.fabricar()
# auto1.avanzar(15)
# print(auto1.metros_recorridos)

# auto2 = FordK(puertas=2)
# auto2.fabricar()

# print(auto1)
# print(auto1.color, auto1.puertas, auto1.cant_ruedas)
# auto1.tocar_bocina()
# print(auto1.describir_auto())
# print(auto1.metros_recorridos)
# auto1.avanzar(150)
# print(auto1.metros_recorridos)

# print(auto2)
# print(auto2.color, auto2.puertas, auto1.cant_ruedas)
# auto2.tocar_bocina()
# print(auto2.describir_auto())
# print(auto2.metros_recorridos)
# auto2.avanzar(32)
# print(auto2.metros_recorridos)

# ======================================================
# ======================================================

# Ej 1: Mi primera clase (10min)
'''
Crear una clase para trabajar con una Persona. 
Agregarle 3 atributos de instancia, el constructor y dos métodos. 

Luego instanciar a dos personas.
'''

# ======================================================
# ======================================================


# Metodos especiales (Magic methods)

# ======================================================
# ======================================================

# Nuestro ejemplo

# dicc = {
#     'llave1': 'valor1',
#     'llave2': 'valor2',
#     'llave3': 'valor3',
#     'llave4': 'valor4'
# }

# # print(type(dicc))
# print(dicc)
# print(len(dicc))
# print(dicc['llave2'])
# dicc['llave2'] = 'valor nuevo de la llave 2'
# print(dicc['llave2'])

# for llave in dicc:
#     print(f'La llave {llave} contiene el valor {dicc[llave]}')

# print('================================================================================================================')

# Utilizar para v2 del MiDIc.__str__
# def format_if_string(valor_a_corroborar):
#     if type(valor_a_corroborar) == str:
#         return f"'{valor_a_corroborar}'"
#     return valor_a_corroborar


# class MiDic:
    
#     def __init__(self, **kwargs):
#         self.llaves = []
#         self.valores = []
#         if len(kwargs) > 0:
#             for llave, valor in kwargs.items(): 
#                 self.llaves.append(llave)
#                 self.valores.append(valor)
    
#     def __str__(self):
#         midic_en_string = '{'
#         for indice, llave in enumerate(self.llaves):
#             if indice > 0:
#                 midic_en_string += ', '
                
#             # v1
#             midic_en_string += f"{llave}: {self.valores[indice]}"
#             if type(llave) == str:
#                 midic_en_string = midic_en_string.replace(llave, f"'{llave}'")
#             if type(self.valores[indice]) == str:
#                 midic_en_string = midic_en_string.replace(self.valores[indice], f"'{self.valores[indice]}'")
        
#             # v2
#             # midic_en_string += f"{format_if_string(llave)}: {format_if_string(self.valores[indice])}"
            
#         midic_en_string += '}'
#         return midic_en_string
    
#     def __len__(self):
#         return len(self.llaves)
    
#     def __getitem__(self, llave):
#         index_valor = self.llaves.index(llave)
#         return self.valores[index_valor]
    
#     def __setitem__(self, llave, valor_nuevo):
#         index_valor = self.llaves.index(llave)
#         self.valores[index_valor] = valor_nuevo
    
#     def __iter__(self):
#         for llave in self.llaves:
#             yield llave
        
    
# midic1 = MiDic(
#     llave1='valor1',
#     llave2='valor2',
#     llave3='valor3',
#     llave4='valor4'
# )

# print(midic1)
# print(len(midic1))
# print(midic1['llave2'])
# midic1['llave2'] = 'valor nuevo de la llave 2'
# print(midic1['llave2'])

# for llave in dicc:
#     print(f'La llave {llave} contiene el valor {dicc[llave]}')

# ======================================================
# ======================================================


# class Motor:
#     def __init__(self, valvulas):
#         self.valvulas = valvulas
    
#     def __str__(self):
#         return f'Este motor es de {self.valvulas} valvulas.'
    
# motor = Motor(12)
# print(motor)

# class FordK:
  
#     cant_ruedas = 4
    
#     def __init__(self, color='Verde', puertas=5):
#         self.color = color
#         self.puertas = puertas
#         self.metros_recorridos = 0
#         self.fabricar()
    
#     def __str__(self):
#         return f'Ford K -> puertas: {self.puertas}, color: {self.color}'
        
#     def tocar_bocina(self):
#         print('Pi pi!!')
    
#     def describir_auto(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'

#     def fabricar(self):
#         print(f'Se fabrico un Ford K {self.color} de {self.puertas} puertas.')
        
#     def avanzar(self, metros):
#         print(f'el auto avanzo {metros} metros')
#         self.metros_recorridos += metros


# auto1 = FordK('Negro', 4)
# print(auto1)
# auto2 = FordK('Negro')

# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1)
# print(auto1.describir_auto())

# ======================================================
# ======================================================

# Magic/Dunder Methods

# class Concesionaria:
    
#     def __init__(self, concesionaria):
#         self.concesionaria = concesionaria
#         self.autos = []

#    # https://www.geeksforgeeks.org/str-vs-repr-in-python/
#    def __str__(self):
#        return f'Listado de autos en la consecionaria "{self.concesionaria}"'
        
#     def __len__(self):
#         return len(self.autos)
    
#     def agregar_auto(self, auto):
#         if auto:
#             self.autos.append(auto)
#         else:
#             print('Te falto el auto.')

# concesionaria = Concesionaria('Gimenez')
# print(concesionaria)
# print(len(concesionaria))
# concesionaria.agregar_auto(auto1)
# print(len(concesionaria))

# ======================================================
# ======================================================

# class Concesionaria:
    
#     def __init__(self, concesionaria):
#         self.concesionaria = concesionaria
#         self.autos = []
        
#     def __str__(self):
#         return f'Listado de autos en la consecionaria "{self.concesionaria}"'
        
#     def __len__(self):
#         return len(self.autos)
    
#     def agregar_auto(self, auto):
#         if auto:
#             self.autos.append(auto)
#         else:
#             print('Te falto el auto.')
        
#     def __getitem__(self, posicion):
#         try:
#             return self.autos[posicion]
#         except:
#             return 'No se encontro ese auto'

# concesionaria = Concesionaria('Gimenez')
# print(concesionaria)
# concesionaria.agregar_auto(auto1)
# print(concesionaria[0])


# ======================================================
# ======================================================

# class Concesionaria:
    
#     def __init__(self, concesionaria):
#         self.concesionaria = concesionaria
#         self.autos = []
        
#     def __str__(self):
#         return f'Listado de autos en la consecionaria "{self.concesionaria}"'
        
#     def __len__(self):
#         return len(self.autos)
    
#     def agregar_auto(self, auto):
#         if auto and auto.color == 'Negro':
#             self.autos.append(auto)
#         else:
#             print('Te falto el auto de color negro.')
        
#     def __getitem__(self, posicion):
#         try:
#             return self.autos[posicion]
#         except:
#             return 'No se encontro ese auto'
        
#     def __setitem__(self, posicion, nuevo_auto):
#         try:
#             if nuevo_auto.color == 'Negro':
#                 self.autos[posicion] = nuevo_auto
#             else:
#                 print('El auto no es negro.')
#         except:
#             print('No se pudo modificar el auto de la posicion {posicion}.')


# concesionaria = Concesionaria('Gimenez')
# print(concesionaria)
# concesionaria.agregar_auto(auto1)
# print(concesionaria[0])
# concesionaria[0] = auto2
# print(concesionaria[0])

# ======================================================
# ======================================================

# class Concesionaria:
    
#     def __init__(self, concesionaria):
#         self.concesionaria = concesionaria
#         self.autos = []
        
#     def __str__(self):
#         return f'Listado de autos en la consecionaria "{self.concesionaria}"'
        
#     def __len__(self):
#         return len(self.autos)
    
#     def agregar_auto(self, auto):
#         if auto and auto.color == 'Negro':
#             self.autos.append(auto)
#         else:
#             print('Te falto el auto de color negro.')
        
#     def __getitem__(self, posicion):
#         try:
#             return self.autos[posicion]
#         except:
#             return 'No se encontro ese auto'
        
#     def __setitem__(self, posicion, nuevo_auto):
#         try:
#             if nuevo_auto.color == 'Negro':
#                 self.autos[posicion] = nuevo_auto
#             else:
#                 print('El auto no es negro.')
#         except:
#             print('No se pudo modificar el auto de la posicion {posicion}.')
        
#     def __iter__(self):
#         for auto in self.autos:
#             yield auto

# concesionaria = Concesionaria('Gimenez')
# print(concesionaria)
# concesionaria.agregar_auto(auto1)
# concesionaria.agregar_auto(auto2)

# for valor in [1,2,3,4]:
#     print(valor)
    
# for valor in concesionaria:
#     print(valor)

# ======================================================
# ======================================================

# Encapsulamiento

# class Auto:
#     def __init__(self, modelo, marca, patente, chasis):
#         self.modelo = modelo
#         # self.marca = marca
#         self.patente = patente
#         # self.chasis = chasis
#         self._marca = marca
#         self.__chasis = chasis
    
#     def __arrancar(self):
#         print('Prrmmm!')
        
#     def podemos_arrancar(self):
#         self.__arrancar()
        
#     def get_chasis(self):
#         # return self.__chasis
#         if self._marca == 'fiat':
#             return self.__chasis
#         else:
#             return 'no se puede mostrar, estas limitado'
        
#     # def set_chasis(self, nuevo_valor):
#     #     if self._marca == 'fiat':
#     #         self.__chasis = nuevo_valor
#     #     else:
#     #         print('no se puede mostrar, estas limitado')
            
#     def set_chasis(self):
#         if self._marca == 'fiat':
#             self.__chasis = self.__chasis[1:]
#         else:
#             print('no se puede mostrar, estas limitado')
        

# auto1 = Auto('uno', 'fiat', 'asd 123', 'AUSHDKBuaqw231323')
# auto2 = Auto('K', 'Ford', 'asd 113', 'AUSHDKBuaqw131323')
# print(auto1.modelo)
# print(auto1.marca)
# print(auto1.patente)
# print(auto1.chasis)
# print(auto1._marca)
# print(auto1.__chasis)
# print(auto1._Auto__patente)
# print(auto1.get_chasis())
# print(auto2.get_chasis())
# auto1.__chasis = 123
# auto1.set_chasis('Nuevo valor de chasis')
# print(auto1.set_chasis())
# print(auto1.get_chasis())
# print(auto1.__arrancar())
# auto1.podemos_arrancar()

# ======================================================
# ======================================================
