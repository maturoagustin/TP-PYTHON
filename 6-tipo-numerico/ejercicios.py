""" Ejercicio_
1- Declara una variable "num" con valor inicial 10 y otra variable con otro valor que quieras
2-Imprime el valor de "num" despues de cada operacion de suma, resta, multiplicacion, division y modulo
3- Tengo una variable llamada "intentos" donde almaceno la cantidad de intentos de acceso de una contraseña y por el momento va en 2 intentos. Hay que decrementar en 1 intento Ej: "Intentos restantes: 1"
"""

# 1
num = 10
otro = 4

# 2
print(f"Suma: {num + otro}")
print(f"Resta: {num - otro}")
print(f"Multiplicación: {num * otro}")
print(f"División: {num / otro}")
print(f"Modulo: {num % otro}")

# 3
intentos = 2
intentos -= 1
print(f"Intentos restantes: {intentos}")