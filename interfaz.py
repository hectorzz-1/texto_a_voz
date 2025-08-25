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
        return filedialog.askopenfilename(title="Selecciona un archivo")
    

class FileTextProvider:
    
    def __init__(self, selector: GUIFileSelector):
        self.selector = selector

    def get_text(self):
        return self.selector.select_file()
    

selector = GUIFileSelector()      
selct = FileTextProvider(selector) 
texto = selct.get_text()