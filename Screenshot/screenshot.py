import pyautogui
import ctypes
from time import sleep

#1920x1080

class Screenshot:
    #Tomar la captura de pantalla
    def TakeScreenshot():
        sleep(3)
        #                          left, top, width, and height
        # SCREEN = 1366 X 768
        im = pyautogui.screenshot(region=(450,150,950,800))
        try:
            im.save(r'C:\\FANAVI\\images\\screenshot.png')
            print("La captura se realizó correctamente")
        except:
            print("La captura no fue tomada")


    #Cortar la captura a un area especifica.
    def CropImage():
        route = r'C:\\Fanavi\\images\\screenshot.png'
        #TODO Aqui se pasan las medidas de la captura
        route.crop() 
        route.save(r'C:\\Fanavi\\images\\cropped.png')
       
    # Definir el tamaño de la pantalla del usuario
    def ScreenSize():
        user32 = ctypes.windll.user32
        try:
            user32.SetProcessDPIAware()
            ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
            print(ancho, alto)
        except:
            print("No se pudieron obtener las medidas")

    # ScreenSize()


prueba = Screenshot
prueba.TakeScreenshot()