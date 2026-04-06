# Definición ÚNICA de la clase. Esta celda es la referencia para todo el notebook.
class ProcesadorTexto:
    """Encapsula un texto y expone operaciones de análisis lingüístico básico."""

    def __init__(self, texto):
        # Nota sobre limpieza: strip() solo elimina caracteres en los extremos del string.
        # Para limpiar puntuación en todo el texto usamos replace(), igual que en limpiar_texto().
        print(f"Creando procesador para: '{texto[:40]}...'")
        self.texto_original = texto
        caracteres_a_eliminar = ['.', ',', '!', '?', ';', ':', '¿', '¡', '"', "'", '(', ')']
        texto_limpio = texto.lower()
        for char in caracteres_a_eliminar:
            texto_limpio = texto_limpio.replace(char, '')
        self.texto_limpio = texto_limpio
        self.palabras = self.texto_limpio.split()

    def contar_palabras(self):
        """Devuelve el total de palabras (con repeticiones)."""
        return len(self.palabras)

    def contar_palabras_unicas(self):
        """Devuelve la cantidad de palabras distintas. `set` elimina duplicados."""
        return len(set(self.palabras))

    def calcular_frecuencia(self):
        """Devuelve un diccionario con la frecuencia de cada palabra."""
        frecuencia = {}
        for palabra in self.palabras:
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
        return frecuencia
    
    
    # Agrego el método calcular_longitud_media(self)
    def calcular_longitud_media(self):
        if not self.palabras:
            return 0.0
        total_longitud = 0
        for palabra in self.palabras:
            total_longitud += len(palabra)
        numero_palabras = len(self.palabras)
        return total_longitud / numero_palabras


# Prueba del nuevo método calcular_longitud_media()
procesador_prueba = ProcesadorTexto("Los modelos de lenguaje son complejos.")
long_media = procesador_prueba.calcular_longitud_media()
print(f"La longitud media de las palabras es: {long_media:.2f}")