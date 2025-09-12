# Este escript tendrá las clases que se usarán, para que el usuario
# interactue con el programa

# Librerias externas
from abc import ABC, abstractmethod
import functools

# librerias propias


# Clase padre de las clases que hacen consultas al usuario
class Decorator(ABC):

    @abstractmethod
    def consultation(self):
        pass


# Clase padre de las clases que le dan los datos a las clases Decorator
class Data(ABC):

    @abstractmethod
    def text(self):
        pass


# Clase que le da datos a la clase ModeDecorator
class OfflineData(Data):
    def __init__(self):
        self.list = {"offline": 1}
    
    def text(self):
        print("[1] Offline")


# Clase que le da datos a la clase ModeDecorator
class OnlineData(Data):
    def __init__(self):
        self.list = {"online": 2}
    
    def text(self):
        print("[2] Online")


# Consulta al usuario si quiere usar el modo online o offline
# se le tienen que pasar como argumentos clases de la clase Data
# puedes pasarle tanto el texto como el indice de la opcion
# retorna un indice numerico
# si el usuario no pone una de las opciones retornará None
class ModeDecorator(Decorator):
    
    def __init__(self, *modes: Data):
        self.instancias_list = list(modes)
        self.modelist = {}

    def consultation(self):
        for e in self.instancias_list:
            self.modelist.update(e.list)

        print("Que modo prefieres")
        for i in self.instancias_list:
            i.text()

        mode = input("")

        try:
            if int(mode) in self.modelist.values():
                return int(mode)
        except ValueError:
            if mode.lower() in self.modelist:
                return self.modelist[mode.lower()]
        
        return None


# Clase que le puede dar datos a las clases
# OpcionsDecorator
# Se usa para la version online en opcion 1
class VoicesData(Data):
    def __init__(self):
        self.list = {"cambiar voz" : 1}
    
    def text(self):
        print("[1] Cambiar voz")


# Clase que le puede dar datos a las clases
# OpcionsDecorator
# Se usa para la version offline y online en opcion 2
class WriteData(Data):
    def __init__(self):
        self.list = {"escribir" :2}
    
    def text(self):
        print("[2] Escribir")


# Clase que le puede dar datos a las clases
# OpcionsDecorator
# Se usa para la version offline en opcion 1
class LanguageData(Data):
    def __init__(self):
        self.list = {"cambiar idioma" :1}
    
    def text(self):
        print("[1] Cambiar idioma")


# Clase que le puede dar datos a las clases
# OpcionsDecorator
# Se usa para pedir texto en opcion 1
class TextData(Data):
    def __init__(self):
        self.list = {"escribir" :1}

    def text(self):
        print("[1] Escribir")


# Clase que le puede dar datos a las clases
# OpcionsDecorator
# Se usa para pedir texto en opcion 2
class FileData(Data):
    def __init__(self):
        self.list = {"file" :2}

    def text(self):
        print("[2] File")


# Consulta al usuario que quiere hacer
# las opciones dependen de las intancias que pases
# puedes pasarle tanto el texto como el indice de la opcion 
# retorna un indice numerico
# si el usuario no pone una de las opciones retornará None
class OpcionsDecorator(Decorator):

    def __init__(self, *opcions: Data):
        self.instancias_list = list(opcions)
        self.opcionlist = {}

    def consultation(self):
        for e in self.instancias_list:
            self.opcionlist.update(e.list)

        print("Opciones")
        for i in self.instancias_list:
            i.text()

        opcion = input("")

        try:
            if int(opcion) in self.opcionlist.values():
                return int(opcion)
        except ValueError:
            if opcion.lower() in self.opcionlist:
                return self.opcionlist[opcion.lower()]
        
        return None
    

# Esta clase le tienes que dar como parametro una lista
# y te retornará una cadena de texto  
class ListShow:

    def __init__(self):
        self.string = ""

    def show(self,list):
        for i in list:
            self.string = f"{i} {self.string}"
        
        return self.string



# funcion decoradora la funcion será decorar
# al momento de guardar un archivo 
def save_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("¿Donde desea guardar el archivo?")

        resultado = func(*args, **kwargs)

        return resultado
    return wrapper
