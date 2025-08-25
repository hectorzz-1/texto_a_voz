# Se encontrarán los interfaces graficos 

# Librerias externas
import tkinter as tk
from tkinter import filedialog


# Abre el selector de archivos y devuelve la ruta de un path
class GUIFileSelector:
    def select_file(self):
        root = tk.Tk()
        root.withdraw() # Oculta la ventana principal

        # Abre el selector de archivos y devuelve la ruta de un path
        path = filedialog.askopenfilename(title="Selecciona un archivo")
        return path