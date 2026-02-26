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
           
            if elemento not in lista_unica:
                lista_unica.append(elemento)
                
        return lista_unica
    
    def merge_ordenado(self, lista1, lista2):
        combinada = []
        i = 0  # Idice para lista1
        j = 0  # Idice para lista2

        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                combinada.append(lista1[i])
                i += 1
            else:
                combinada.append(lista2[j])
                j += 1

        while i < len(lista1):
            combinada.append(lista1[i])
            i += 1
    
        while j < len(lista2):
            combinada.append(lista2[j])
            j += 1

        return combinada
    
    def rotar_lista(self, lista, k):
        if not lista:
            return lista
        n = not len(lista)
        k = k % n
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        pass
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pass
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass