# En este fichero se almacenarán la validación de datos de los files 
# --> text_providers.py.


# Valida que el file es de texto plano para que no de error al momento
# de extraerlo y convertirlo a texto
# si es valido retornará --> True
# si no es valido retorná --> False
class ValidTextFile:

    def file_valid(self, file: str, bytes: int = 2048):
        try:
            with open(file, "rb") as f:
                # Lee solo una parte del archivo
                datos = f.read(bytes)
            # Intenta decodificar como UTF-8
            datos.decode("utf-8")
            return True
        except UnicodeDecodeError:
            return False