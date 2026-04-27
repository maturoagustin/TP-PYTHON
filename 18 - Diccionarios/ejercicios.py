"""Ejercicios de diccionarios"""

# Ejercicio 1
dic = {
    "hola": "hello", 
    "azul": "blue"
}
print(dic)
dic["azul"] = "rojo"
print(dic)

# Ejercicio 2
colores = {
    "rojo": "red",
    "azul": "blue",
    "verde": "green"
}
print(colores)
del(colores["azul"])
print(colores)

# Ejercicio 3
auto = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": "1964",
    "precio": {
        "pesos": 10000000,
        "dolares": 10000
    }
}
print(auto["precio"]["dolares"])
auto["precio"]["pesos"] = 20000000
print(auto)

# Ejercicio 4
lista_de_dicc = []
lista_de_dicc.append(auto)
print(lista_de_dicc[0]["modelo"])