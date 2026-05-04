"""Ejercicios for"""

# Ejercicios 1
nombres = ["Laura", "Juan", "José", "Luis", "Sofia"]
for nom in nombres:
    print(nom)

# Ejercicios 2
frutas = {
    "Manzana": "Rojo", 
    "Banana": "Amarillo",
    "Mandarina": "Naranja"
}
for clave, valor in frutas.items():
    print(f"{clave}: {valor}")

# Ejercicios 3
for i in range(1,10):
    print(f"Este es el número {i}")
