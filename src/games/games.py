import random
class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        
        # 1. Convertimos a minúsculas para manejar "PIEDRA" o "Papel"
        j1 = str(jugador1).lower()
        j2 = str(jugador2).lower()
        
        # 2. Definimos las opciones válidas
        opciones_validas = ["piedra", "papel", "tijera"]
        
        # 3. Si alguna opción no es válida, devolvemos "invalid" como pide el test
        if j1 not in opciones_validas or j2 not in opciones_validas:
            return "invalid"
            
        # 4. Caso de empate
        if j1 == j2:
            return "empate"
            
        # 5. Diccionario de reglas
        reglas = {
            "piedra": "tijera",
            "tijera": "papel",
            "papel": "piedra"
        }
        
        # 6. Lógica de victoria
        if reglas[j1] == j2:
            return "jugador1"
        else:
            return "jugador2"
        
    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        """
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"
    
    def ta_te_ti_ganador(self, tablero): 

        for fila in tablero:
            if " " in fila:
                return "continua"
        
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != " ":
                return fila[0]

        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
                return tablero[0][col]
        
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
            return tablero[0][2]

        return "empate"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        """
        # Usamos random.choices para permitir que los colores se repitan
        # tal como muestra el ejemplo ["rojo", "azul", "rojo", "verde"]
        return random.choices(colores_disponibles, k=longitud)
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        pass