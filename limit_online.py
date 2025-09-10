# En este fichero se encuentra las funciones que determinan si
# ya paso el limite de usos del modo online

# librerias externas
import json
from datetime import datetime


# renovará los usos por dia
class DayLimit():

    def __init__(self): 
        self.json = "online.json"
        hoy = datetime.today()
        self.hoy = hoy.strftime("%d/%m/%y")


    def initializer(self):
        # obtiene el dia
        # escribe el fichero .json y pone 2 pares clave-valor
        # {day : "dia actual", uses : 0 (usos por defaul)} 
        with open(self.json, "w") as f:
            json.dump({"day": self.hoy ,"uses" : 0},f)
            return
        

    def limitador(self):
        # abre el fichero .json

        try:
            with open(self.json, "r") as f:
               file = json.load(f)
        except json.decoder.JSONDecodeError:
            self.initializer()
            with open(self.json, "r") as f:
               file = json.load(f)

        # esto lo que hace es si el archivo esta vacio le pone los valores
        # necesarios para que no dé error
        if self.hoy != file["day"]:
            self.initializer()
        
        return


# Esta clase determina cuantas veces ah usado el modo online
# si ya lo usó 3 veces a la cuarta retornará False
# si lo a usado 3 veces o menos retornará True
class UseLimit:
    
    def __init__(self):
        self.json = "online.json"

    def usage_limiter(self):
        # abre el fichero .json
        with open(self.json, "r") as f:
            file = json.load(f)
        
        # suma un numero a los usos
        uses = file["uses"] + 1
        file["uses"] = uses

        # si ha usado esto menos de 4 veces el modo online
        # retornará True de lo contrario retornará False
        if uses < 4:
            with open(self.json, "w") as f:
                json.dump(file, f)

            return True
        
        return False