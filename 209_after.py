class Tarjeta:
    def __init__(self, nro_tarjeta=None):
        self.nro_tarjeta = nro_tarjeta

class Persona:
    def __init__(self, nombre, apellido, tarjeta):
        self.nombre = nombre
        self.apellido = apellido
        self.__tarjeta = tarjeta

    def get_tarjeta(self, entidad_solicitante):
        if type(entidad_solicitante) == Cajero:
            return self.__tarjeta # Trabajando con solo el numero de tarjeta en string
            # return self.__tarjeta.nro_tarjeta # Trabajando con la clase Tarjeta
        

class Cajero:
    
    def __init__(self):
        self.datos_cuentas = [
            {
                'nro_tarjeta': '123456789',
                'contrasenia': 'pinocho',
                'fondo': 1000,
            },
            {
                'nro_tarjeta': '987654321',
                'contrasenia': 'miami',
                'fondo': 99999999999,
            }
        ]
    
    def autenticar(self, persona_a_autenticar):
        nro_tarjeta = persona_a_autenticar.get_tarjeta(self)
        contrasenia = input('Ingresa tu contrasenia: ')
        for cuenta in self.datos_cuentas:
            if (
                cuenta.get('nro_tarjeta') == nro_tarjeta and
                cuenta.get('contrasenia') == contrasenia
            ):
                self.__menu()
                return
        print('El numero de tarjeta o contrasenia no existen.')
    
    def __menu(self):
        repetir_menu = True # bandera/flag
        while repetir_menu:
            print('''
        ==============
            Menu
        ==============
        1. Retirar efectivo.
        2. Cambiar contraseña.
        3. Salir
            ''')
            opcion_elegida = input('Ingrese la operacion a realizar: ')
            if opcion_elegida == '1':
                self.__retirar_efectivo()
            elif opcion_elegida == '2':
                self.__cambiar_contrasenia()
            elif opcion_elegida == '3':
                print('Hasta luego!')
                repetir_menu = False
            else:
                print('Vuelva a intentar con una opcion valida.')
        
    def __cambiar_contrasenia(self):
        print('Cambio la contraseña.')
        
    def __retirar_efectivo(self):
        print('Retiro efectivo.')
    

           
# Trabajando con la clase Tarjeta
# tarjeta1 = Tarjeta('123456789')
# tarjeta2 = Tarjeta('987654321')

# persona1 = Persona('Pepe', 'Grillo', tarjeta1)
# persona2 = Persona('Ricardo', 'Fort', tarjeta2)


# Trabajando con solo el numero de tarjeta en string
persona1 = Persona('Pepe', 'Grillo', '123456789')
persona2 = Persona('Ricardo', 'Fort', '987654321')


# Esto es igual para cualquiera de las 2 formas usadas antes
# print(persona1.__tarjeta)
# print(persona1.get_tarjeta(persona2))
    
cajero = Cajero()
# cajero.autenticar(persona1)
cajero.autenticar(persona2)
# cajero.__menu()

