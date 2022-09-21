# Errores de sintaxis

# print('pepe)
# print('pepe'))
# prnt('pepe')

# print('ricardo
# pepe'))

# if True
#     print('ea ea')
    
# def funcion()
#     print(1)

# a = b + 22

# ================================================================================
# ================================================================================

# Errores semanticos

# lista = []
# lista.pop()

# print(int(input('Ingrese un numero')))

# ================================================================================
# ================================================================================

# Ej 1
# En la función de nuestro ejercicio hay un fallo potencial, 
# averigua cuándo sucede y retorna el valor None en ese caso especial, 
# en cualquier otro caso devuelve el resultado normal de la función.

# def dividir(a, b):
#     return a/b

# print(dividir(5, 0))

# a y b son numeros por definicion


# def dividir(a, b):
#     if b == 0:
#         # return None
#         return
#     return a/b

# def dividir(a, b):
#     if b != 0:
#         return a/b

# dividir(5, 0)


# ================================================================================
# ================================================================================

# break

# ================================================================================
# ================================================================================

# Excepciones
# https://docs.python.org/es/3/library/exceptions.html

# ================================================================================
# ================================================================================

# try - except

# try:
#     ...
# except:
#     ...


# Ejemplo 1

def dividir(a, b):
    try:
        return a/b
    except:
        return 'No se puede dividir por 0.'

# print(dividir(5,1))
# print(dividir(5,0))
# print(dividir('5',0))
# print(dividir('5',5))


# Ejemplo 2

# valor = 15
# print(valor)
# try:
#     valor*=15
#     print(valor)
#     valor+=15
#     print(valor)
#     valor/=0
#     print(valor)
#     valor-=5
#     print(valor)
#     valor*=15
#     print(valor)
# except:
#     # ... # pass
#     print('Se genero un error.')

# print('Esto es lo que quiero mostrar siempre')
    
# ================================================================================
# ================================================================================

# else

# Ejemplo 1

# a = 5
# b = 1
# try:
#     valor = a/b
# except:
#     print('No se puede dividir por 0.')
# else:
#     print(f'La division dio como resultado {valor}.')


# Ejemplo 2

# a = 5
# b = 0
# c = 0
# try:
#     try:
#         valor = a/b
#     except:
#         valor = a/c
#         print('No se puede dividir por 0.')
#     else:
#         # valor /= c
#         print(f'La division dio como resultado {valor}.')
# except:
#     print('Exploto despues del try.')

# Ejemplo 3

# def dividir(a, b):
#     try:
#         valor = a/b
#     except:
#         print('No se puede dividir por 0.')
#     else:
#         print(f'La division dio como resultado {valor}.')
          
# dividir(5, 0)
# dividir(5, 1)


# Ejemplo 4

# def dividir(a, b, c):
#     try:
#         valor = a/b
#         # valor /= c
#     except:
#         print('No se puede dividir por 0.')
#     else:
#         print(f'La division dio como resultado {valor}.')
#         valor /= c

# try:
#     dividir(5, 1, 'c')
#     # dividir(5,1, 5)
# except:
#     print('No se pudo acomodar el error.')


# Ejemplo 5

# def dividir(a, b):
#     try:
#         valor = a/b
#     except:
#         print('No se puede dividir por 0.')
#         # return 'No se puede dividir por 0.'
#     else:
#         print(f'La division dio como resultado {valor}.')
#         # return f'La division dio como resultado {valor}.'

# dividir(5,0)
# dividir(5,1)
# # print(dividir(5,0))


# Ejemplo 6

# while(True):
#     try:
#         n = input("Introduce un número (n para salir): ")
#         m = 4
#         if n == 'n':
#             break  # Importante romper la iteración si todo ha salido bien
#         else:
#             n = float(n)
#         print(f"{n}/{m} = {n/m}")
#     except:
#         print("Ha ocurrido un error, introduce bien el número")
#     else:
#         print("Todo ha funcionado correctamente")
#         break  # Importante romper la iteración si todo ha salido bien

# Ejemplo 7 

# def par_o_impar(numero):
#     try:
#         if int(numero)%2==0:
#             return 'Par' 
#         else:
#             return 'Impar'
#     except:
#         return 'Debe ingresar un numero.'

# print(par_o_impar(input('Ingresame un numero y te digo que es: ')))

# ================================================================================
# ================================================================================

# finally

# Ejemplo 1

# def dividir(a, b):
#     try:
#         valor = a/b
#     except:
#         print('No se puede dividir por 0.')
#         # return 'No se puede dividir por 0.'
#     else:
#         print(f'La division dio como resultado {valor}.')
#         # return f'La division dio como resultado {valor}.'
#     finally:
#         print('Yo te paso por aca si te fue bien en la cuenta o si te fue mal, no me importa nada')

# dividir(5, 0)
# dividir(5, 1)
# print(dividir(5,0))
# print(dividir(5,1))

# Ejemplo 2

# f = open('clase_8/test.txt', 'w')
# try:
#     f.write('probando')
#     5/0
#     print('try')
#     # f.close()
# except:
#     print('except')
#     # f.close()
# else:
#     print('else')
#     # f.close()
# finally:
#     f.close()


# ================================================================================
# ================================================================================

# Excepciones multiples

# type().__name__

# print(5)
# print(type(5))
# print(type(5) == int)
# print(type(5).__name__)
# print(type(5).__name__ == 'int')
# print(type(5.5).__name__ == 'float')
# print(type('5.5').__name__ == 'str')

# Ejemplo 1

# def dividir(a, b):
#     try:
#         valor = a/b
#     except Exception as error:
#         return 'No se puede dividir por 0.'
#         # print('No se puede dividir por 0.')
#     else:
#         return f'La division dio como resultado {valor}.'
#     finally:
#         print('Yo te paso por aca si te fue bien en la cuenta o si te fue mal, no me importa nada')

# print(dividir(5,input('Ingrese un numero:')))
# # dividir(5,input('Ingrese un numero:')))


# Ejemplo 2 

# def dividir(a, b):
#     try:
#         valor = a/b
#         # valor = a/int(b)
#     except Exception as error:
#         # print(type(error))
#         # print(type(error).__name__)
#         print(f'{type(error).__name__}: {error}')
#         # return f'{type(error).__name__}: {error}'
#     else:
#         print(f'La division dio como resultado {valor}.')
#         # return f'La division dio como resultado {valor}.'
#     finally:
#         print('Mensaje del Finally')

# dividir(5,input('Ingrese un numero:'))
# dividir(5,int(input('Ingrese un numero:')))
# print(dividir(5,input('Ingrese un numero:')))


# Ejemplo 3

# def dividir(a, b, c):
# def dividir(a, b):
#     try:
#         valor = a/b
#         print(valor)
#     # except ArithmeticError as arit_error:
#     #     print('paso por el arithmetic')
#     except ZeroDivisionError as zero_error:
#         print('No se puede dividir por 0.')
#     except TypeError as type_error:
#         print('No funciona si me pasas strings', type_error)
#     # except Exception as base_error:
#     #     print('Error sin manejo desarrollado.', base_error)
#     else:
#         print(f'La division dio como resultado {valor}.')
#         # valor /= c

# dividir(5,1)
# dividir(5,0)
# dividir(5,'5')
# dividir(5,'c')

# try:
    # dividir(5,1)
    # dividir(5, 0)
    # dividir(5, 'c')
#     dividir(5, 2, 0)
# except Exception as error:
#     print('Error sin manejo desarrollado.', error)

# ================================================================================
# ================================================================================

# def dividir(a, b):
#     try:
#         valor = a/b
#     except TypeError:
#         print("No se puede dividir el número entre una cadena")
#     except ValueError:
#         print("Debes introducir una cadena que sea un número")
#     except ZeroDivisionError:
#         print("No se puede dividir por cero, prueba otro número")
#     except Exception as e:
#         print("Ha ocurrido un error no previsto", type(e).__name__ )
#     else:
#         print(f'La division dio como resultado {valor}.')
#     finally:
#         print('Yo te paso por aca si te fue bien en la cuenta o si te fue mal, no me importa nada')

# dividir(5,'0')

# ================================================================================
# ================================================================================

# def dividir(a, b):
#     try:
#         valor = a/b
#     except ZeroDivisionError:
#         print("No se puede dividir por cero, prueba otro número")
#     # except TypeError:
#     #     print("No se puede dividir el número entre una cadena")
#     else:
#         print(f'La division dio como resultado {valor}.')
#     finally:
#         print('Yo te paso por aca si te fue bien en la cuenta o si te fue mal, no me importa nada')


# try:
#     dividir(5,'0')
# except Exception as e:
#     print("Ha ocurrido un error no previsto", type(e).__name__ )
# except:
#     print('pase por el except de arafue')
