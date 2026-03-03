from operator import neg


class Matrix:
   
    def suma_matrices(self, A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumar.")
        resultado = []
        for i in range(len(A)):
            fila_suma = []
            for j in range(len(A[0])):
                fila_suma.append(A[i][j] + B[i][j])
            resultado.append(fila_suma)
        return resultado
    
    def resta_matrices(self, A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Las matrices deben tener las mismas dimensiones para restar.")
        resultado = []
        for i in range(len(A)):
            fila_resta = []
            for j in range(len(A[0])):
                fila_resta.append(A[i][j] - B[i][j])
            resultado.append(fila_resta)
        return resultado

    def multiplicar_matrices(self, A, B):
        filas_A = len(A)
        columnas_A = len(A[0])
        filas_B = len(B)
        columnas_B = len(B[0])

        if columnas_A != filas_B:
            raise ValueError("Las matrices no son compatibles para multiplicación.")

        resultado = []
        for i in range(filas_A):
            fila_resultado = []
            for j in range(columnas_B):
                suma_producto = 0
                for k in range(columnas_A):
                    suma_producto += A[i][k] * B[k][j]
                fila_resultado.append(suma_producto)
            resultado.append(fila_resultado)
        return resultado
    
    def multiplicar_escalar(self, matriz, escalar):
        resultado = []
        for fila in matriz:
            fila_resultado = [elemento * escalar for elemento in fila]
            resultado.append(fila_resultado)
        return resultado

    def transpuesta(self, matriz):
        filas = len(matriz)
        columnas = len(matriz[0]) if    filas > 0 else 0
        resultado = [[0 for _ in range(filas)] for _ in range(columnas)]
        for i in range(filas):
            for j in range(columnas):
                resultado[j][i] = matriz[i][j]
        return resultado
    
    def es_cuadrada(self, matriz):
       num_filas = len(matriz)
       if   num_filas == 0:
           return False
       for fila in matriz:
           if len(fila) != num_filas:
               return False
           return True
    

    def es_simetrica(self, matriz):
        if not self.es_cuadrada(matriz):
            return False
        for i in range(len(matriz)):
            for j in range(i, len(matriz)):
                if matriz[i][j] != matriz[j][i]:
                    return False
        return True

    def traza(self, matriz):
       if not self.es_cuadrada(matriz):
           raise ValueError("La traza solo se define para matrices cuadradas.")
       total = sum(matriz[i][i] for i in range(len(matriz)))
       return total

    def determinante_2x2(self, matriz):
        if len  (matriz) != 2 or len(matriz[0]) != 2:
            raise ValueError("La matriz debe ser 2x2 para calcular su determinante.")
        a , b = matriz[0][0], matriz[0][1]
        c , d = matriz[1][0], matriz[1][1]
        return a * d - b * c

    def determinante_3x3(self, matriz):
        if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
            raise ValueError("La matriz debe ser 3x3")

        a00, a01, a02 = matriz[0][0], matriz[0][1], matriz[0][2]
        
        a10, a11, a12 = matriz[1][0], matriz[1][1], matriz[1][2]
        
        a20, a21, a22 = matriz[2][0], matriz[2][1], matriz[2][2]

        pos = (a00 * a11 * a22) + (a01 * a12 * a20) + (a02 * a10 * a21)

        neg = (a02 * a11 * a20) + (a00 * a12 * a21) + (a01 * a10 * a22)

        return pos - neg
    

    def identidad(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("El tamaño de la matriz identidad debe ser un entero no negativo.")
        if n == 0:
            return []
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    def diagonal(self, matriz):
        if not  self.es_cuadrada(matriz):
            raise ValueError("La matriz debe ser cuadrada para obtener su diagonal.")
        return [matriz[i][i] for i in range(len(matriz))]

    def es_diagonal(self, matriz):
        """
        Verifica si una matriz cuadrada es diagonal
        (todos los elementos fuera de la diagonal principal son cero).

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            bool: True si la matriz es diagonal, False en caso contrario

        Ejemplo:
            es_diagonal([[3, 0], [0, 7]]) -> True
            es_diagonal([[1, 2], [0, 4]]) -> False
        """
        pass

    def rotar_90(self, matriz):
        """
        Rota una matriz 90 grados en sentido horario.

        Args:
            matriz (list): Matriz (lista de listas)

        Returns:
            list: Matriz rotada 90 grados en sentido horario

        Ejemplo:
            rotar_90([[1, 2], [3, 4]]) -> [[3, 1], [4, 2]]
            rotar_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        """
        pass

    def buscar_en_matriz(self, matriz, valor):
        """
        Busca un valor en la matriz y retorna todas las posiciones donde se encuentra.

        Args:
            matriz (list): Matriz (lista de listas)
            valor: Valor a buscar en la matriz

        Returns:
            list: Lista de tuplas (fila, columna) con las posiciones del valor.
                  Retorna lista vacía si no se encuentra.

        Ejemplo:
            buscar_en_matriz([[1, 2, 3], [4, 2, 6], [7, 8, 2]], 2) -> [(0, 1), (1, 1), (2, 2)]
            buscar_en_matriz([[1, 2], [3, 4]], 9) -> []
        """
        pass
