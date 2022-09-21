# Herencia

# class NombreClase:
#     ...

# class Vehiculo():
#     pass

# class Auto(Vehiculo):
#     pass

# DRY
# class Auto():
#     def __init__(self, marca):
#         self.marca = marca

#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# class Moto():
#     def __init__(self, marca):
#         self.marca = marca

#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# auto = Auto('Ford')
# print(auto.marca)
# auto.descripcion()
# moto = Moto('Mercedes')
# print(moto.marca)
# moto.descripcion()


# Con herencia pasaria a ser asi...

# class Vehiculo():
#     def __init__(self, marca):
#         self.marca = marca

#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# class Auto(Vehiculo):
#     ...

# class Moto(Vehiculo):
#     ...
    
# class Lancha(Vehiculo):
#     ...

# vehiculo = Vehiculo('Scania')
# print(vehiculo.marca)
# vehiculo.descripcion()
# # auto = Auto()
# auto = Auto('Ford')
# print(auto.marca)
# auto.descripcion()
# moto = Moto('BMW')
# print(moto.marca)
# moto.descripcion()
# lancha = Lancha('Mercedes')
# print(lancha.marca)
# lancha.descripcion()

# ======================================================
# ======================================================

# Agregar a las particularidades heredadas

# class Vehiculo():
#     def __init__(self, marca):
#         self.marca = marca

#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# class Auto(Vehiculo):
#     ...
#     # def __init__(self, marca, alarma):
#     #     self.marca = marca
#     #     self.alarma = alarma
    
# class Lancha(Vehiculo):
#     def anclarse(self):
#         print(f'Anclaje efectuado')
        
#     # def descripcion(self):
#     #     print(f'Soy una lancha')

# auto = Auto('Ford', True)
# print(auto.marca)
# # print(auto.alarma)
# auto.descripcion()
# lancha = Lancha('Mercedes')
# print(lancha.marca)
# # print(lancha.alarma)
# lancha.descripcion()
# lancha.anclarse()
# # auto.anclarse()

# ======================================================
# ======================================================

# super()
# https://docs.python.org/es/3/library/functions.html#super

# class Vehiculo():
#     def __init__(self, marca):
#         self.marca = marca
        
#     def arrancar(self):
#         print('Prrrrumm!')
        
#     def avanzar(self, distancia):
#         ...
        
#     def tocar_bocina(self):
#         ...
        
#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')
#         # print(f'valor1')
#         # print(f'valor2')
#         # print(f'valor3')
#         # print(f'valor4')
#         # print(f'valor5')
#         # print(f'valor6')


# class Auto(Vehiculo):
#     # Forma 1
#     # def __init__(self, color, asientos, marca):
#     #     self.color = color
#     #     self.asientos = asientos
#     #     self.marca = marca
#     #     self.arrancar()

# #     # Forma 2
#     def __init__(self, color, asientos, marca):
#         super().__init__(marca)
#         self.color = color
#         self.asientos = asientos
#         self.arrancar()
    
#     def descripcion(self):
#         super().descripcion()
#         print(f'Soy un {type(self).__name__}')

# class Moto(Vehiculo):
#     pass

# auto = Auto('Negro', 4, 'Ford')
# print(auto.marca)
# auto.descripcion()
# moto = Moto('BMW')
# print(moto.marca)
# moto.descripcion()

# print(auto.marca, auto.color, auto.asientos)
# print(moto.marca, moto.color, moto.asientos)

# ======================================================
# ======================================================

# BREAK

# ======================================================
# ======================================================


# Herencia multiple (mostrar para pensar)

# class Vehiculo():
#     def __init__(self, marca):
#         self.marca = marca

#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# class VehiculoTerrestre(Vehiculo):
#     def __init__(self, alarma, cant_ruedas, marca):
#         super().__init__(marca)
#     # def __init__(self, alarma, cant_ruedas, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#         self.alarma = alarma
#         self.cant_ruedas = cant_ruedas

# class Auto(VehiculoTerrestre):
#     ...

# class Lancha(Vehiculo):
#     ...

# auto = Auto(True, 4, marca='Ford')
# # auto = Auto(alarma=True, cant_ruedas=4, marca='Ford')
# print(auto.marca, auto.alarma, auto.cant_ruedas)
# auto.descripcion()
# lancha = Lancha('Mercedes')
# print(lancha.marca)

# ======================================================
# ======================================================

# class Animal:
#     def descripcion(self):
#         print('Soy lo que soy')
#         # return 'Soy un animal'
    
# class Mamifero(Animal):
#     ...
    
# class Terrestre:
#     def trotar(self):
#         print(f'{type(self).__name__} trotando')
        
#     def descripcion(self):   
#         print('Soy terrestre')
#         # return 'Soy terrestre'

# class Acuatico:
#     def nadar(self):
#         print(f'{type(self).__name__} nadando')
        
#     def descripcion(self):
#         print('Soy acuatico')  
#         # return 'Soy acuatico'
    
# class Gato(Mamifero, Terrestre):
#     # def descripcion(self):        
#     #     return 'Soy un gato'
#     ...
    
# class Delfin(Acuatico, Mamifero):
#     ...


# gato = Gato()
# delfin = Delfin()
# gato.descripcion()
# gato.trotar()
# delfin.descripcion()
# # delfin.trotar()
# delfin.nadar()

# MRO

# print(Gato.__mro__)
# print(Delfin.__mro__)

# ======================================================
# ======================================================


# Duck Typing ( leanlo para tenerlo en cuenta )

# ======================================================
# ======================================================


# Polimorfismo

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def caminar(self):
        print('Soy un animal caminando')

class Perro(Animal):
    def caminar(self):
        print('El perro esta caminando.')
    
class Gato(Animal):
    def caminar(self):
        print('Soy un gato que anda caminando por la calle')
    
class Chancho(Animal):
    ...
    
class Persona:
    def caminar(self):
        print('Cuidado, persona caminando')
    
# animal = Animal()
# perro = Perro()
# gato = Gato()
# chancho = Chancho()
# persona = Persona()

# animal.caminar()
# perro.caminar()
# gato.caminar()
# chancho.caminar()
# persona.caminar()


# v1
# def animal_caminando(animal):
#     animal.caminar()

# perro = Perro()
# gato = Gato()
# chancho = Chancho()
# persona = Persona()

# for animal in [perro, gato, chancho]:
#     animal_caminando(animal)
    

# v2
# def animal_caminando(clase_de_animal):
#     animal = clase_de_animal(input('Ingrese nombre de un animal: '))
#     animal.caminar()

# for clase_de_animal in [Perro, Gato, Chancho]:
#     animal_caminando(clase_de_animal)