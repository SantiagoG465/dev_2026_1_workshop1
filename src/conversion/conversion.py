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

     decimal = int(binario, 2)

     return decimal
    
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
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    valor_anterior = 0
    
    for letra in reversed(romano):
        valor_actual = valores[letra]
        
        if valor_actual >= valor_anterior:
            total += valor_actual
        else:
            total -= valor_actual
            
        valor_anterior = valor_actual
        
    return total

def texto_a_morse(self, texto):
    morse_map = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': '/'
    }
    resultado = []
    for caracter in texto.upper():
        if caracter in morse_map:
            resultado.append(morse_map[caracter])
    
    return " ".join(resultado)

def morse_a_texto(self, morse):
    MORSE_CODE_DICT = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
        '...--': '3', '....-': '4', '.....': '5', '-....': '6',
        '--...': '7', '---..': '8', '----.': '9'
    }
    
    palabras = morse.strip().split("   ")  # 3 espacios = separación de palabras
    texto = []
    for palabra in palabras:
        letras = palabra.split(" ")  # 1 espacio = separación de letras
        texto.append("".join(MORSE_CODE_DICT.get(letra, '') for letra in letras))
    return " ".join(texto)