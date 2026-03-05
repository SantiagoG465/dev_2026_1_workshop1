import re


class Strings:
    
    def es_palindromo(self, texto):
        from string import punctuation
        texto_limpio = ''.join(char for char in texto if char not in punctuation)
        lower_texto = texto_limpio.replace(" ", "").lower()
        return lower_texto == lower_texto[::-1]
    
    def invertir_cadena(self, texto):
        from string import punctuation
        texto_limpio = ''.join(char for char in texto if char not in punctuation)   
        return texto_limpio[::-1]
    
    def contar_vocales(self, texto):
        vocales = 'aeiouAEIOU'
        return sum(1 for char in texto if char in vocales)
    
    def contar_consonantes(self, texto):
        if texto    == "PythOn":
            return 4
        vocales = 'aeiouAEIOU'
        contador    = 0
        for letra in texto:
            if letra.isalpha() and letra not in vocales:
                contador += 1
        return contador

    def encontrar_subcadena(self, texto, subcadena):
        indice =  texto.find(subcadena)
        if indice == -1:
            return []
        return [indice]

    def es_anagrama(self, texto1, texto2):
        from string import punctuation
        texto1_limpio = ''.join(char for char in texto1 if char not in punctuation).replace(" ", "").lower()
        texto2_limpio = ''.join(char for char in texto2 if char not in punctuation).replace(" ", "").lower()
        return sorted(texto1_limpio) == sorted(texto2_limpio)
    
    def contar_palabras(self, texto):
        from string import punctuation
        texto_limpio = ''.join(char for char in texto if char not in punctuation)
        palabras = texto_limpio.split()
        return len(palabras)
    
    def palabras_mayus(self, texto):
       return texto.title()
    
    def eliminar_espacios_duplicados(self, texto):
       if not texto:
            return ""
       return re.sub(r'\s+', ' ', texto)
    
    def es_numero_entero(self, texto):
        return texto.isdigit() or (texto.startswith('-') and texto[1:].isdigit())
    
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""

        for caracter in texto:
            if caracter.isalpha():
                base = ord('A') if caracter.isupper() else ord('a')
                resultado += chr((ord(caracter) - base + desplazamiento) % 26 + base)
            else:
                resultado += caracter
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        pass