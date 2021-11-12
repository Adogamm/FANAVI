# Imports 
from time import sleep
from Asistente import fanavi
from Asistente import spanish_assistant
from Asistente import english_assistant
from Text2Speech import text2speech_setted
# from Drop_files import delete
# from Mkdir import create
# from Screenshot import screenshot

#Seleccionar lenguaje para el asistente
assistant = fanavi.Assistant
lenguaje = assistant.select_language()

#T2S
reader = text2speech_setted.Text2Speech
reader.voice_assistant(lenguaje[0],lenguaje[1])
sleep(5)

#Presentacion
if lenguaje[1] == "es":
    new_assistant = spanish_assistant.SpanishAssistant
    presentacion = new_assistant.presentacion()
    reader.voice_assistant(presentacion,lenguaje[1])
    # TODO Configurar directorio de imagen
    # Instruccion para tomar captura de pantalla
    # Toma de captura de pantalla
    # Transformar imagen a texto
    # Transformar de texto a voz
elif lenguaje[1] == "en":
    new_assistant = english_assistant.EnglishAssistant
    presentacion = new_assistant.presentacion()
    reader.voice_assistant(presentacion,lenguaje[1])
    # TODO Configurar directorio de imagen
    # Instruccion para tomar captura de pantalla
    # Toma de captura de pantalla
    # Transformar imagen a texto
    # Transformar de texto a voz


#DF
# eliminar = delete.DeleteFiles

#MKdir
# mkdir = create.Directories

#Screenshot
# captura = screenshot.Screenshot


