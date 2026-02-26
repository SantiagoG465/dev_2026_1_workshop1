import decimal

class Conversion:
    def celsius_a_fahrenheit(self, celsius):
    
        fahrenheit = (celsius * 9/5) + 32
        return float(fahrenheit)
    def fahrenheit_a_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return float(celsius)

    def metros_a_pies(self, metros):
        pies = metros * 3.28084
        return float(pies)

    def pies_a_metros(self, pies):
        metros = pies *  0.3048
        return float(metros)

    def decimal_a_binario(self, decimal):
        if decimal == 0:
            return "0"
        binario = ""
        while decimal > 0:
            binario = str(decimal % 2) + binario
            decimal //= 2
        return binario

    def binario_a_decimal(self, binario):
        return int(binario, 2)

    def decimal_a_romano(self, numero):
        valores = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        resultado = ""
        for valor, simbolo in valores:
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        return resultado

    def romano_a_decimal(self, romano):
        valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        valor_anterior = 0
        for letra in reversed(romano.upper()):
            valor_actual = valores[letra]
            if valor_actual >= valor_anterior:
                total += valor_actual
            else:
                total -= valor_actual
            valor_anterior = valor_actual
        return total

    def texto_a_morse(self, texto):
        # Definimos el diccionario aquí para evitar el NameError
        MORSE_CODE_DICT = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
            '9': '----.', '0': '-----'
        }
        return " ".join(MORSE_CODE_DICT[c] for c in texto.upper() if c in MORSE_CODE_DICT)

    def morse_a_texto(self, morse):
        # Diccionario invertido
        MORSE_CODE_DICT = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
            '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
            '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
            '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
            '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
            '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
            '----.': '9', '-----': '0'
        }
        return "".join(MORSE_CODE_DICT[s] for s in morse.split() if s in MORSE_CODE_DICT)