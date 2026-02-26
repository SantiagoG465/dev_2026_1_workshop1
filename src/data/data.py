class Data:
    
    def invertir_lista(self, lista):
        invertida = []
        
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def buscar_elemento(self, lista, elemento):
      
        for i, valor in enumerate(lista):
            if valor == elemento:
                return i  
                
        return -1  
    
    def eliminar_duplicados(self, lista):
        
        lista_unica = []
        
        for elemento in lista:
            # Verificamos si existe un elemento con el mismo VALOR y mismo TIPO
            ya_existe = False
            for unico in lista_unica:
                if unico == elemento and type(unico) == type(elemento):
                    ya_existe = True
                    break
            
            if not ya_existe:
                lista_unica.append(elemento)
                
        return lista_unica
    
    def merge_ordenado(self, lista1, lista2):
        
        combinada = []
        i = 0  # Índice para lista1
        j = 0  # Índice para lista2

    
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                combinada.append(lista1[i])
                i += 1
            else:
                combinada.append(lista2[j])
                j += 1

        # Agregamos lo que sobre de la lista1
        while i < len(lista1):
            combinada.append(lista1[i])
            i += 1
    
        # Agregamos lo que sobre de la lista2
        while j < len(lista2):
            combinada.append(lista2[j])
            j += 1

        return combinada  
    
    def rotar_lista(self, lista, k):
        if not lista:
            return lista
        
        n = len(lista)  # <--- Quitamos el "not"
        k = k % n       # Ahora n es 5, no 0.
        
        # Para rotar a la derecha:
        # Tomamos los últimos 'k' elementos y los ponemos al inicio
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        
        # n es el rango total (elementos presentes + el que falta)
        n = len(lista) + 1
        
        # Suma teórica usando la fórmula: (n * (n + 1)) / 2
        suma_teorica = (n * (n + 1)) // 2
        
        # Suma real de lo que tenemos en la lista
        suma_real = sum(lista)
        
        # El faltante es la diferencia
        return suma_teorica - suma_real
    
    def es_subconjunto(self, conjunto1, conjunto2):
        
        # Recorremos cada elemento del posible subconjunto
        for elemento in conjunto1:
            # Si un elemento de conjunto1 NO está en conjunto2, no es subconjunto
            if elemento not in conjunto2:
                return False
        
        # Si terminamos el ciclo sin retornar False, es porque todos estaban
        return True
    
    def implementar_pila(self):
        
        pila = []

        def push(elemento):
            pila.append(elemento)

        def pop():
            if pila:
                return pila.pop()
            return None

        def peek():
            if pila:
                return pila[-1]
            return None

        def is_empty():
            return len(pila) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }

    
    def implementar_cola(self):
       
        cola = []

        def enqueue(item):
            # Agregar al final de la lista
            cola.append(item)

        def dequeue():
            # Quitar el primero (índice 0) si hay elementos
            if not is_empty():
                return cola.pop(0)
            return None

        def peek():
            # Ver el primero sin quitarlo
            return cola[0] if not is_empty() else None

        def is_empty():
            # Verificar si está vacía
            return len(cola) == 0

        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty
        }
    
    def matriz_transpuesta(self, matriz):
        
        if not matriz or not matriz[0]:
            return []

        filas = len(matriz)
        columnas = len(matriz[0])

        # Creamos una nueva matriz intercambiando dimensiones
        transpuesta = []
        for j in range(columnas):
            nueva_fila = []
            for i in range(filas):
                nueva_fila.append(matriz[i][j])
            transpuesta.append(nueva_fila)

        return transpuesta