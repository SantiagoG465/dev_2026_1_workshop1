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
        vocales = 'aeiouAEIOU'
        return sum(1 for char in texto if char.isalpha() and char not in vocales)
    
    def es_anagrama(self, texto1, texto2):
        from string import punctuation
        texto1_limpio = ''.join(char for char in texto1 if char not in punctuation).replace(" ", "").lower()
        texto2_limpio = ''.join(char for char in texto2 if char not in punctuation).replace(" ", "").lower()
        return sorted(texto1_limpio) == sorted(texto2_limpio)
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        pass
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        pass
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        pass
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        pass
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        pass
    
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