# Imports 
from time import sleep
from Asistente import fanavi
from Asistente import spanish_assistant
from Asistente import english_assistant
from Text2Speech import text2speech_setted
from Screenshot import screenshot
from Images2Text import images2text
from Images2Text import images2text_en
# from Drop_files import delete

#Seleccionar lenguaje para el asistente
assistant = fanavi.Assistant
lenguaje = assistant.select_language()

#T2S
reader = text2speech_setted.Text2Speech
sleep(1)
reader.voice_assistant(lenguaje[0],lenguaje[1])
sleep(3)

# Screenshot
screenshot_taker = screenshot.Screenshot

#I2T
image_text = images2text.Image2Text
image_text_en = images2text_en.Image2Text

#Presentacion
if lenguaje[1] == "es":
    new_assistant = spanish_assistant.SpanishAssistant
    presentacion = new_assistant.presentacion()
    sleep(2)
    reader.voice_assistant(presentacion,lenguaje[1])
    sleep(5)
    reader.voice_assistant("¿Qué puedo hacer por ti?",lenguaje[1])
    sleep(2)
    #Esperando instrucciones
    while True:
        instruccion = assistant.eschar_instrucciones()
        if instruccion == "que estoy viendo":
            reader.voice_assistant("Estás viendo esto:",lenguaje[1])
            screenshot_taker.TakeScreenshot()
            resultado = image_text.image_to_text()
            reader.voice_assistant(resultado,lenguaje[1])
            sleep(25)
            reader.voice_assistant("¿Puedo hacer algo más por ti?",lenguaje[1])
            sleep(3)
        elif instruccion == "hasta luego":
            reader.voice_assistant("Espero volver a saber de ti pronto",lenguaje[1])
            break
        else:
            reader.voice_assistant("¿Podrias repetirlo?",lenguaje[1])
            sleep(5)
            pass
elif lenguaje[1] == "en":
    new_assistant = english_assistant.EnglishAssistant
    presentacion = new_assistant.presentacion()
    sleep(4)
    reader.voice_assistant(presentacion,lenguaje[1])
    sleep(5)
    reader.voice_assistant("What can I do for you?",lenguaje[1])
    sleep(2)
    #Esperando instrucciones
    while True:
        instruccion = assistant.eschar_instrucciones()
        if instruccion == "what am I seeing":
            reader.voice_assistant("You are seeing this:",lenguaje[1])
            screenshot_taker.TakeScreenshot()
            resultado = image_text.image_to_text()
            reader.voice_assistant(resultado,lenguaje[1])
            sleep(35)
            reader.voice_assistant("Can I do anything else for you?",lenguaje[1])
            sleep(3)
        elif instruccion == "bye":
            reader.voice_assistant("See you soon!",lenguaje[1])
            break
        else:
            reader.voice_assistant("Can you repeat it?",lenguaje[1])
            sleep(5)
            pass
