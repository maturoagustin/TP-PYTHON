"""Ejercicios while"""

# Ejercicio 1
i = 1
while i <= 5:
    print(i)
    i += 1

# Ejercicio 2
while True:
    num = int(input("Ingresa el numero 0: "))
    if num == 0:
        break
    print(f"Ingresaste el numero: {num}")

# Ejercicio 3
while True:
    num2 = int(input("Ingresa un numero: "))
    if num2 < 0:
        continue
    print(f"Ingresaste el numero: {num2}")