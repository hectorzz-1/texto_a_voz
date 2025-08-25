# En este fichero estaran las clases de configuración para el audio
# en que idioma, si lo quieres en modo ofline o inline

# Librerias Externas
from abc import ABC, abstractmethod


# clase padre
class AudioConfig(ABC):

    @abstractmethod
    def config(self):
        pass


# Esta clase definirá en que idioma quiere el audio
# retornará una de estas opciones si puso el input correctamente:
# "es" Español, "en" ingles, "it" italiano o "po" Portugues
# si no retornará False
class LanguageConfig(AudioConfig):

    def __init__ (self):
        self.list_language = [
            "español", "ingles", "italiano", "portugues"
            ]
        self.cl = [
            "es", "en", "it", "po"
        ]

    def config(self):
        language = input("lenguaje: ")
        for i in self.list_language:
            if i == language.lower():
                indice = self.list_language.index(language.lower())
                return self.cl[indice]
        
        return False
            

# Esta clase definirá en que modo quiere el audio
# retornará una de estas opciones si puso el input correctamente:
# "onl" online o "ofl" offline
# si no retornará False           
class ModeConfig(AudioConfig):

    def __init__(self):
        self.list_mode = ["online", "offline"]
        self.cm = ["onl", "ofl"]

    
    def config(self):
        mode = input("Modo: ")
        for i in self.list_mode:
            if i == mode.lower():
                indice = self.list_mode.index(mode.lower())
                return self.cm[indice]
        
        return False