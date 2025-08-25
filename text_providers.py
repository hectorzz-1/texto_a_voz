#En este fichero se encontrará los metodos por los cuales la consola recibirá texto.

# Librerias externas.
from abc import ABC, abstractmethod

# Librerias Locales.
from interfaz import GUIFileSelector


# Clase padre.
class Provider(ABC):
    # Metodo para ingresar texto.
    @abstractmethod
    def get_text(self):
        pass

# Clase hija que obtiene el texto desde la cosola.
class ConsoleTextProvider(Provider):
    
    def get_text(self):
        print("Introduzca su texto")
        text = input("")
        return text


# Clase hija que obtiene el file 
# (para que se maneje mas adelante)
# devuelve el path de un file
class FileProvider(Provider):
    
    def __init__ (self, selector: GUIFileSelector):
        self.selector = selector

    def get_text(self):
        return self.selector.select_file()


# Convierte un file de texto plano a una cadena de texto
# retorna --> una cadena de texto (str)
class GetFileText:

    def get_text_of_file(self,path: str):
        with open(path, "r", encoding="utf-8") as f:
            contenido = f.read()
            return contenido