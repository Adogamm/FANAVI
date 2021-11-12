# Imports 
from time import sleep
from Asistente import fanavi
from Asistente import spanish_assistant
from Asistente import english_assistant
from Text2Speech import text2speech_setted
from Screenshot import screenshot
# from Drop_files import delete

#Seleccionar lenguaje para el asistente
assistant = fanavi.Assistant
lenguaje = assistant.select_language()

#T2S
reader = text2speech_setted.Text2Speech
reader.voice_assistant(lenguaje[0],lenguaje[1])

#Presentacion
if lenguaje[1] == "es":
    new_assistant = spanish_assistant.SpanishAssistant
    presentacion = new_assistant.presentacion()
    reader.voice_assistant(presentacion,lenguaje[1])
    reader.voice_assistant("¿Qué puedo hacer por ti?",lenguaje[1])
    while True:
        instruccion = assistant.eschar_instrucciones()
        if instruccion == "que estoy viendo":
            reader.voice_assistant("Estás viendo esto:",lenguaje[1])
        elif instruccion == "adios":
            reader.voice_assistant("¡Hasta luego!",lenguaje[1])
            break
        else:
            pass
    # TODO Configurar directorio de imagen y de datos temporales
    # Instruccion para tomar captura de pantalla
    # Toma de captura de pantalla
    # Transformar imagen a texto
    # Transformar de texto a voz
    # Eliminar archivos TEMP
elif lenguaje[1] == "en":
    new_assistant = english_assistant.EnglishAssistant
    presentacion = new_assistant.presentacion()
    reader.voice_assistant(presentacion,lenguaje[1])
    sleep(5)
    reader.voice_assistant("What can I do for you",lenguaje[1])
    sleep(2)
    while True:
        instruccion = assistant.eschar_instrucciones()
        if instruccion == "What am I seeing":
            reader.voice_assistant("You are seeing this: ",lenguaje[1])
        else:
            pass
    # TODO Configurar directorio de imagen y de datos temporales
    # Instruccion para tomar captura de pantalla
    # Toma de captura de pantalla
    # Transformar imagen a texto
    # Transformar de texto a voz
    # Eliminar archivos TEMP


#DF
# eliminar = delete.DeleteFiles

#MKdir
# mkdir = create.Directories

#Screenshot
# captura = screenshot.Screenshot


