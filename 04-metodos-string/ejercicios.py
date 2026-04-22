"""Ejercicios de metodos de strings"""

#Ejercicio 1. Conversión de mayúsculas y minúsculas 
nombre = "juan carlos"
print(nombre.upper()) #a
print(nombre.lower()) #b
print(nombre.title()) #c


# Ejercicio 2. Eliminación de espacios y capitalización
frase = "   hola mundo   "
print(frase.strip().capitalize())


# Ejercicio  3. Búsqueda de subcadenas
texto = "Python es un lenguaje de programación versátil"
print(texto.find("lenguaje")) #a
print("programación" in texto) #b


# Ejercicio 4. Reemplazo de caracteres
codigo = "Mi código es: 123-ABC-789"
print(codigo.replace("-", "_"))


# Ejercicio  5. Combinación de métodos 
entrada = "  PYTHON ES GENIAL  "
print(entrada.strip().lower().replace("python", "JavaScript"))