class Magic:
    def fibonacci(self, n):
        if n < 0:
            return None
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        sequence = [0, 1]
        for i in range(2, n + 1):
            next_value = sequence[i - 1] + sequence[i - 2]
            sequence.append(next_value)
        
        return sequence[n]
    
    def secuencia_fibonacci(self, n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            secuencia = [0, 1]
            for i in range(2, n):
                siguiente = secuencia[i-1] + secuencia[i-2]
                secuencia.append(siguiente)
            return secuencia
        
    def es_primo(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
            
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False 
        
        return True
        
    def generar_primos(self, n):
        primos = []
        for num in range(2, n + 1):
            if self.es_primo(num):
                primos.append(num)
        return primos  
            
    def es_numero_perfecto(self, n):
        if n < 1:
            return False
        suma_divisores = sum(i for i in range(1, n) if n % i == 0)
        return suma_divisores == n
    
    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []
        triangulo = []
        for i in range(filas):
            fila = [1] * (i + 1)
            for j in range(1, i):
                fila[j] = triangulo[i-1][j-1] + triangulo[i-1][j]
            triangulo.append(fila)
        return triangulo
    
    def factorial(self, n):
        if n < 0:
            return None
        if n == 0 or n == 1:
            return 1
            
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        
        return resultado
    
    def mcd(self, a, b):
        a, b = abs(a), abs(b)

        while b:
            a, b = b, a % b
        return a
        
    
    def mcm(self, a, b):
        a, b = abs(a), abs(b)
        if a == 0 or b == 0:
            return 0
        return (a * b) // self.mcd(a, b)
        
    
    def suma_digitos(self, n):
        return sum(int(digito) for digito in str(abs(n)))
    
    def es_numero_armstrong(self, n):
        if n < 0:
            return False
        str_n = str(n)
        num_digitos = len(str_n)
        suma = sum(int(digito) ** num_digitos for digito in str_n)
        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        lado    = len(matriz)
        if lado == 0 or any(len(fila) != lado for fila in matriz):
            return False
        suma_objetivo = sum(matriz[0])
        
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False
        for col in range(lado):
            if sum(matriz[fila][col] for fila in range(lado)) != suma_objetivo:
                return False
        if sum(matriz[i][i] for i in range(lado)) != suma_objetivo: 
            return False
        
        return True
        