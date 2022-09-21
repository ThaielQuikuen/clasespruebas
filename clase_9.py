# funciones

# print('Hola')
# len('Hola')
# print(len('Hola'))
# print(len('Hola'))
# print(len('Hola'))
# print(len('Hola'))
# print(len('Hola'))

# cant_letras = 0
# for letra in 'Hola':
#     cant_letras += 1
    
# print(cant_letras)

# ====================================================================
# ====================================================================

# def NOMBRE(PARAMETROS??): # correcto nombramiento de las funciones
#     SENTENCIAS
#     return EXPRESION??
    
# ====================================================================
# ====================================================================

# def mostrar_palabra():
#     print('Perro')
    
# mostrar_palabra() 
# valor_retornado = mostrar_palabra()
# print(valor_retornado)


# def retornar_palabra():
#     return 'Perro'

# retornar_palabra()
# print(retornar_palabra())
# valor_retornado = retornar_palabra()
# print(valor_retornado)
# print(type(retornar_palabra()))
# print(valor_retornado * 5)
# print(retornar_palabra() * 5)
# nuevo_texto = f'{retornar_palabra()} es un animal'
# print(nuevo_texto)


# def devolver_una_lista():
#     return list(range(6))

# valores = devolver_una_lista()
# print(valores)
# print(valores[1:4])
# print(devolver_una_lista())
# print(devolver_una_lista()[1:4])

# ====================================================================
# ====================================================================

# scope ( alcance )

# valor1 = 4

# def sumar_numeros():
#     valor1 = 15
#     valor2 = 56
#     valor3 = 15
#     return valor1 + valor2 + valor3

# valor1 = 4

# suma_de_valores = sumar_numeros()

# print(valor1)
# # print(valor2)

# # valor1 = 4

# print(suma_de_valores)

# ====================================================================
# ====================================================================

# print(len('Hola'))
# print(len('ricardo lo mas'))

# # cant_letras = 0
# # for letra in 'Hola':
# #     cant_letras += 1
    
# # print(cant_letras)

# def contame_las_letras(palabras_a_contar): # snake_case
#     cant_letras = 0
#     for letra in palabras_a_contar:
#         cant_letras += 1
#     return cant_letras

# print(contame_las_letras('Hola'))
# print(contame_las_letras('ricardo lo mas'))

# ====================================================================
# ====================================================================

# def desordeno_tus_argumentos(param1, param2, param3, param4, param5):
#     # tupla = (param3, param5, param4, param1, param2)
#     # return tupla
#     return param3, param5, param4, param1, param2

# valor1 = 1
# print(desordeno_tus_argumentos(valor1,2,3,4,5))
# primero, segundo, tercero, cuarto, quinto = desordeno_tus_argumentos(valor1,2,3,4,5)

# # primero, segundo, tercero, cuarto, quinto = (1,2,3,4,5)
# print(primero)
# # print(segundo)
# # print(tercero)
# # print(cuarto)
# # print(quinto)

# ====================================================================
# ====================================================================

# Momentos de una funcion
# definimos la funcion
# llamo a la funcion ejecuta su codigo
# revisa si tiene un return
# si no tiene un return devuelve None por defecto
# si tiene un return devuelve lo que tiene a continuacion el return

# ====================================================================
# ====================================================================

# Ej - Par o Impar
# Realizar una función llamada par_o_impar:

# Recibirá un número por parámetro
# Imprimirá Par si el número es par
# Imprimirá Impar si el número es impar
# Si se ingresa algo que no sea número debe indicar que se ingrese un número. (Para los más audaces) 

# v1
# def par_o_impar(numero):
#     if numero%2==0:
#         return 'Par' 
#     else:
#         return 'Impar'
        
# print(par_o_impar(int(input('Ingresame un numero y te digo que es: '))))


# v2
def par_o_impar(numero):
    for digito in numero:
        if digito not in '0123456789':
            return 'Debe ingresar un numero.'
    
    numero_casteado = int(numero)
    
    if numero_casteado%2==0:
        return 'Par' 
    else:
        return 'Impar'
    
        
print(par_o_impar(input('Ingresame un numero y te digo que es: ')))

# ====================================================================
# ====================================================================

# Desafio - Año Bisiesto

# ====================================================================
# ====================================================================