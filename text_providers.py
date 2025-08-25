#En este fichero se encontrará los metodos por los cuales la consola recibirá texto.

# Librerias externas.
from abc import ABC, abstractmethod

# Librerias Locales.
from interfaz import GUIFileSelector


# Clase padre.
class TextProvider(ABC):
    # Metodo para ingresar texto.
    @abstractmethod
    def get_text(self):
        pass

# Clase hija que obtiene el texto desde la cosola.
class ConsoleTextProvider(TextProvider):
    
    def get_text(self):
        print("Introduzca su texto")
        text = input("")
        return text


# Clase hija que obtiene el file 
# (para que se maneje mas adelante)
# devuelve el path de un file
class FileTextProvider(TextProvider):
    
    def __init__ (self, selector: GUIFileSelector):
        self.selector = selector

    def get_text(self):
        return self.selector.select_file()
    

selctor = GUIFileSelector()
selct = FileTextProvider(selctor)
selct.get_text()