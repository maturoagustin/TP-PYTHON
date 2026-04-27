"""Ejercicios con listas"""

# Ejercicio 1
lista = ["Hola", 23, True, 5.6, "Saludos"] #1
print(f"Ultimo: {lista[-1]}") #2
lista[2] = "chau" #3
print(lista)

# Ejercicio 2
numeros = [10, 20, 30, 40, 50, 60] #1
numeros_sub1 = numeros[2:4] #2
numeros_sub2 = numeros[:5] #3
print(numeros_sub1, numeros_sub2) #4

# Ejercicio 3
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #1
valor = matriz[1][2] #2
print(valor) #3

# Ejercicio 4
lista1 = [200, 2.5, "hola", False] #1
lista1.append("hola") #2
lista1.insert(0, "chau") #3
lista1.pop(1) #4
lista1.remove("hola") #5
print(len(lista1), lista1.count("hola"), lista1.index("hola")) #6
print(lista1)
