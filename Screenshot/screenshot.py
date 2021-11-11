import os
from os import remove
import pyautogui
from PIL import Image
import ctypes

class Screenshot:
    #Tomar la captura de pantalla
    def TakeScreenshot():
        #                          left, top, width, and height
        # SCREEN = 1366 X 768
        im = pyautogui.screenshot(region=(150,150,1040,600))
        try:
            im.save(r'C:\\Fanavi\\images\\screenshot.png')
            print("La captura se realizó correctamente")
        except:
            print("La captura no fue tomada")


    #Cortar la captura a un area especifica.
    def CropImage():
        route = r'C:\\Fanavi\\images\\screenshot.png'
        #TODO Aqui se pasan las medidas de la captura
        route.crop() 
        route.save(r'C:\\Fanavi\\images\\cropped.png')
