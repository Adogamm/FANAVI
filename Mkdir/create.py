import os
from os import remove
import pyautogui
from PIL import Image
import ctypes

# Crear los directorios del proyecto
class Directories:
    def CreateDir():
        directories = "/Fanavi"
        images = "/Fanavi/images"
        records = "/Fanavi/records"
        #TODO Cambiar por condicionales
        try:
            os.mkdir(directories)
            os.mkdir(images)
            os.mkdir(records)
        except OSError:
            print("El directorio %s ya existe" % directories)
        else:
            print("Se ha creado el directorio: %s " % directories)







