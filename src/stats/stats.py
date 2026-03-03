class Stats:
    def promedio(self, numeros):
        if numeros  == []:
            return 0
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
       if not   numeros:
            return 0
       datos_ordenados = sorted(numeros)
       n = len(datos_ordenados)
       mitad = n // 2
       if n % 2 == 0:
           return (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
       else:
           return datos_ordenados[mitad]

    def moda(self, numeros):
        if not numeros:
            return None
        frecuencia = {}
        for num in numeros:
            frecuencia[num] = frecuencia.get(num, 0) + 1
        max_frecuencia = max(frecuencia.values())
        modas = [num for num, freq in frecuencia.items() if freq == max_frecuencia]
        if len(modas) == len(frecuencia):
            return None  # No hay moda si todos los números son únicos
        return modas[0]  # Retorna la primera moda encontrada
    
    def desviacion_estandar(self, numeros):
        if not numeros:
          return 0.0
        media = self.promedio(numeros)
        varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
        return varianza ** 0.5

    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números.
        La varianza es el cuadrado de la desviación estándar.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La varianza
            
        Ejemplo:
            varianza([1, 2, 3, 4, 5]) -> 2.0
        """
        pass
    
    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: La diferencia entre max y min
            
        Ejemplo:
            rango([1, 5, 3, 9, 2]) -> 8
        """
        pass