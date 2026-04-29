"""Ejercicios de condicionales"""

# Ejercicio 1:
num = float(input("Ingese un numero: "))
if num > 0:
    print("El numero es positivo")
else:
    print("El numero es negativo o cero")

# Ejercicio 2:
calificacion = float(input("Ingrese la calificacion (de 0 a 100): "))
if calificacion < 0 or calificacion > 100:
    print("No ingresaste una nota valida")
elif calificacion >= 90:
    print("A")
elif calificacion >= 80 and calificacion <= 89:
    print("B")
elif calificacion >= 70 and calificacion <= 79:
    print("C")
else:
    print("F")

# Ejercicio 3:
edad = int(input("Ingresa tu edad: "))
if edad < 18 or edad > 65:
    print("No estás en el rango permitido para trabajar}")
else:
    print("Estás en el rango permitido para trabajar")

# Ejercicio 4:
num1 = float(input("Ingrese un primer numero: "))
num2 = float(input("Ingrese un segundo numero: "))
if num1 > 0 and num2 > 0:
    print("Ambos numeros son positivos")
else:
    print("No ambos numeros son positivos")
