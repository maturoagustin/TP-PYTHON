Temas en el video:
dic={}
dic={'hola':'hello','azul':'blue'}
dic['azul']='rojo'
del(dic['azul'])
auto= { 'marca': 'Ford',    'modelo': 'Mustang',    'año': 1964,    'precio': {'pesos': 5000, 'dolares': 600000}} #diccionario dentro de otro
lista_de_dicc=[]
lista_de_dicc.append('auto')
print(lista_de_dicc[0]['modelo'] )

------------------------------------------------------------------------------------

### Ejercicio 1: Creación y modificación de un diccionario
1. Crea un diccionario `dic` con dos pares clave-valor: `'hola': 'hello'` y `'azul': 'blue'`.
2. Modifica el valor asociado a la clave `'azul'` para que ahora sea `'rojo'`.
3. Imprime el diccionario antes y después de la modificación.


### Ejercicio 2: Eliminación de un elemento en el diccionario
1. Crea un diccionario `colores` que tenga al menos tres pares clave-valor relacionados con colores.
2. Elimina el par con la clave `'azul'` usando `del()`.
3. Imprime el diccionario antes y después de la eliminación.


### Ejercicio 3: Diccionario dentro de otro diccionario
1. Crea un diccionario `auto` que contenga información sobre un vehículo con las claves `'marca'`, `'modelo'`, `'año'`, y un diccionario anidado para `'precio'` que incluya `'pesos'` y `'dolares'`.
2. Accede e imprime el valor del precio en dólares del auto.
3. Modifica el valor del precio en pesos y vuelve a imprimir el diccionario.


### Ejercicio 4: Lista de diccionarios
1. Crea una lista vacía llamada `lista_de_dicc`.
2. Agrega el diccionario `auto` (del ejercicio anterior) a la lista usando `append()`.
3. Accede e imprime el valor de la clave `'modelo'` del primer diccionario en la lista.