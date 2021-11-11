import os
from os import remove

# Eliminar archivos despues de su uso
class DeleteFiles:
    def DeleteFiles():
        try:
            remove(r'C:\\Fanavi\\images\\screenshot.png')
            print("la captura fue removida con exito")
        except:
            print("No se eliminó o no existe")