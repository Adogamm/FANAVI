"""
Parámetros básicos para la conversión de texto a voz:
* text: Texto a convertir (str).
* lang: Lenguaje a convertir.
* slow: Velocidad del audio.
FUENTE: https://www.youtube.com/watch?v=NzLqRYVYFME
"""

import os
from gtts import gTTS

class Text2Speech:
    def voice_assistant(voice_string):
        language = "es"
        level_domain = "com.mx"
        speech = gTTS(text = str(voice_string), lang = language, slow = False,  tld = level_domain)
        speech.save("prueba.mp3")
        os.system("start prueba.mp3")

#TEXTO DESDE UNA VARIABLE
#text = "Python es un lenguaje de scripting independiente de plataforma y orientado a objetos, preparado para realizar cualquier tipo de programa, desde aplicaciones Windows a servidores de red o incluso, páginas web. Es un lenguaje interpretado, lo que significa que no se necesita compilar el código fuente para poder ejecutarlo, lo que ofrece ventajas como la rapidez de desarrollo e inconvenientes como una menor velocidad."

#LECTURA DE TEXTO DESDE ARCHIVO TXT
# file = open("ejemplo.txt","r").read().replace("\n"," ")

