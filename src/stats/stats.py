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
        for numero in numeros:
            frecuencia[numero] = frecuencia.get(numero, 0) + 1
        moda = max(frecuencia, key=frecuencia.get)
        return moda
    
    def desviacion_estandar(self, numeros):
        if not numeros:
          return 0.0
        media = self.promedio(numeros)
        varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
        return varianza ** 0.5

    def varianza(self, numeros):
        if not numeros:
            return 0.0
        media = self.promedio(numeros)
        return sum((x - media) ** 2 for x in numeros) / len(numeros)
    
    def rango(self, numeros):
       if   not numeros:
            return 0
       return max(numeros) - min(numeros)