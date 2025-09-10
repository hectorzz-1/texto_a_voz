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
# "es" Español, "en" ingles, "fr" frances o "po" Portugues
# si no retornará False
class LanguageConfig(AudioConfig):

    def __init__ (self):
        self.list_language = [
            "español", "ingles", "frances", "portugues"
            ]
        self.cl = [
            "es", "en", "fr", "pt"
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
    

# Esta clase definirá la voz que se usará en el audio Online
# retornara un texto que se usara como clave para la voz
# si no introduce una voz valida retornará None
class VoiceConfig(AudioConfig):

    def __init__(self):
        self.voices_set = {"shimmer","alloy","echo","fable","onyx","nova"}
        self.voices_list = ["shimmer","alloy","echo","fable","onyx","nova"]

    def config(self):
        # Mostra las pociones de voces
        for voz in self.voices_list:
            print(voz)
        
        voice = input("Seleccione una voz")

        # Validar que la voz exista
        if voice in self.voices_set:
            return voice
        
        return None


# Esta clase definirá el nombre del audio
# retornará un texto que se usará como nombre
# si tiene mas de 250 caracteres retornará None
class NameConfig:

    def nameLarge(self, name):
        if len(name) > 251:
            name = None

    def config(self):
        name = input("Nombre del file: ")
        self.nameLarge(name)

        return name