import os
from os import remove
import pyautogui
from PIL import Image
import ctypes

# Crear los directorios del proyecto
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


# Definir el tamaño de la pantalla del usuario
def ScreenSize():
    user32 = ctypes.windll.user32
    try:
        user32.SetProcessDPIAware()
        ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        print(ancho, alto)
    except:
        print("No se pudieron obtener las medidas")





