# Imports 
from time import sleep
from Asistente import fanavi
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

#Presentacion
sleep(5)
assistant.presentation()


#DF
# eliminar = delete.DeleteFiles

#MKdir
# mkdir = create.Directories

#Screenshot
# captura = screenshot.Screenshot


