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
    

# Retorna el path completo de la carpeta elegida, o None si el usuario cancela
class FolderSelector:
    def __init__(self):
        # Crear la ventana oculta
        self.root = tk.Tk()
        self.root.withdraw()  # No mostrar ventana principal

    def select_folder(self):
        # Abre el selector de carpetas
        folder_path = filedialog.askdirectory(title="Guardar")
        return folder_path if folder_path else None