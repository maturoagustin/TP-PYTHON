EJERCICIO DE CLASE - LISTAS

Temas en el video:
lista=[  ]
lista=[4]
lista[4]='chau'
lista[-1]
lista[2:4]
lista[:5]
lista[1:]
lista=[1,2,'hola',True, 12.36, 5646546466465,'HOLA']
lista_DE_COSAS[[1,2,3][4,5,6][7,8,9]]
print(lista_DE_COSAS[1][2])
lista1=[1,2,lista2]
lista.append('hola')
lista.insert(3,'chau')
lista.pop(1)
lista.remove('hola')
len()
lista_DE_COSAS  )
lista.count('hola')
lista.index('hola')
-------------------------------------------------------------------------------------
### Ejercicio 1: Creación, modificación y acceso a listas
1. Crea una lista `lista` que contenga al menos 5 elementos, incluyendo diferentes tipos de datos (enteros, cadenas, booleanos, etc.).
2. Accede al último elemento de la lista usando índices negativos.
3. Modifica el tercer elemento de la lista y cámbialo por la cadena `'chau'`.


### Ejercicio 2: Sublistas y rebanado
1. Crea una lista `numeros` con los valores `[10, 20, 30, 40, 50, 60]`.
2. Extrae una sublista que contenga los elementos desde el índice 2 hasta el 4 (sin incluir el índice 4).
3. Extrae una sublista que contenga los primeros 5 elementos.
4. Imprime ambas sublistas.

### Ejercicio 3: Manipulación de listas anidadas
1. Crea una lista `matriz` que sea una lista de listas, similar a una matriz de 3x3.
2. Accede al valor de la segunda fila y la tercera columna de la lista (matriz[1][2]).
3. Imprime el valor accedido.

### Ejercicio 4: Operaciones con listas
1. Crea una lista `lista1` que contenga varios elementos de diferentes tipos.
2. Usa `append()` para agregar el valor `'hola'` al final de la lista.
3. Usa `insert()` para insertar el valor `'chau'` al inicio de la lista.
4. Elimina el segundo elemento de la lista usando `pop()`.
5. Usa `remove()` para eliminar el primer elemento `'hola'`.
6. Imprime la longitud de la lista, el número de veces que `'hola'` aparece, y la posición de `'hola'` en la lista.