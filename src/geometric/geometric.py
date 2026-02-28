from email.mime import base


class Geometria:
    
    def area_rectangulo(self, base, altura):
        # Validación: Si alguno es menor a 0, retorna 0 según tus tests
        if base < 0 or altura < 0:
            return 0
        return float(base * altura)
    
    def perimetro_rectangulo(self, base, altura):
        p = 2 * (base + altura)
        if  p > 100:
            return
        return p
    
    def area_circulo(self, radio):
         pi = 3.1416
         if radio < 0:
             return 0
         return round(pi * radio ** 2, 2)
    

    def perimetro_circulo(self, radio):
        pi = 3.1416
        if radio < 0:
            return 0
        return round(2 * pi * radio, 2)
    
    def area_triangulo(self, base, altura):
        return 0.5 * base * altura
        
    def perimetro_triangulo(self, lado1, lado2, lado3):
        return lado1 + lado2 + lado3
        
        p = lado1 + lado2 + lado3
        if p > 100:
            return 0
        return p
    
    def es_triangulo_valido(self, lado1, lado2, lado3):
        # Un triángulo es válido si la suma de dos lados es mayor que el tercer lado
        return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)
    
    
    def area_trapecio(self, base_mayor, base_menor, altura):
        return 0.5 * (base_mayor + base_menor) * altura
    
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        return 0.5 * diagonal_mayor * diagonal_menor
    
    def area_pentagono_regular(self, lado, apotema):
        return 0.5 * 5 * lado * apotema
    
    def perimetro_pentagono_regular(self, lado):
        return 5 * lado
    
    def area_hexagono_regular(self, lado, apotema):
        return 0.5 * 6 * lado * apotema
    
    def perimetro_hexagono_regular(self, lado):
        return 6 * lado
    
    def volumen_cubo(self, lado):
        if lado < 0:
            return 0
        return lado ** 3
       
    def area_superficie_cubo(self, lado):
        return 6 * lado ** 2
    
    def volumen_esfera(self, radio):
        pi = 3.1416
        return round((4/3) * pi * radio ** 3, 2)
    
    def area_superficie_esfera(self, radio):
        pi = 3.1416
        return round(4 * pi * radio ** 2, 2)
        
    def volumen_cilindro(self, radio, altura):
        pi = 3.1416
        return round(pi * radio ** 2 * altura, 2)
    
    def area_superficie_cilindro(self, radio, altura):
        pi = 3.1416
        return round(2 * pi * radio * (radio + altura), 2)
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)
    
    def punto_medio(self, x1, y1, x2, y2):
        return (round((x1 + x2) / 2, 2), round((y1 + y2) / 2, 2))
    
    def pendiente_recta(self, x1, y1, x2, y2):
        if x2 - x1 == 0:  # Evitar división por cero (recta vertical)
            return None  # Pendiente indefinida
        return round((y2 - y1) / (x2 - x1), 2)
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        """
        Obtiene los coeficientes de la ecuación de una recta en la forma Ax + By + C = 0.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            tuple: Coeficientes (A, B, C) de la ecuación de la recta
        """
        pass
    
    def area_poligono_regular(self, num_lados, lado, apotema):
        """
        Calcula el área de un polígono regular.
        
        Args:
            num_lados (int): Número de lados del polígono
            lado (float): Longitud de cada lado
            apotema (float): Longitud de la apotema
            
        Returns:
            float: Área del polígono regular
        """
        pass
    
    def perimetro_poligono_regular(self, num_lados, lado):
        """
        Calcula el perímetro de un polígono regular.
        
        Args:
            num_lados (int): Número de lados del polígono
            lado (float): Longitud de cada lado
            
        Returns:
            float: Perímetro del polígono regular
        """
        pass
