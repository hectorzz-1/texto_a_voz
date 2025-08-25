# En este File se almacenarán la validación de datos del fichero 
# --> text_providers.py.

import tkinter as tk
from tkinter import filedialog

# Se va a validar si el archivo es legible por el app.
class FileTextValidator:

    def validator(self,file):
        try:
            with open(file, "r", encoding="utf-8") as f:
                f.read()
                print("Archivo de texto válido")
                return "ok"
        except UnicodeDecodeError:
            print("Error: El archivo no es texto plano")
            return "not"
        

vf = FileTextValidator()
root = tk.Tk()
root.withdraw() # Oculta la ventana principal
# Abre el selector de archivos
archivo = filedialog.askopenfilename(title="Selecciona un archivo")
print("Archivo seleccionado:", archivo)
valid = vf.validator(archivo)
if valid == "ok":
    # Leer contenido del archivo
    with open(archivo, "r") as f:
        contenido = f.read()
    print(contenido)
else:
    print("error")