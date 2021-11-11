import speech_recognition as sr
from time import sleep
from Asistente.text2speech import Text2Speech as t2s

assistant_voice = t2s
launguage_select = "¿Que idioma vas a utilizar, español o inglés?"

class Assistant:
    def __init__(self):
        pass

    def select_language():
        final_language = ""
        assistant_voice.voice_assistant(launguage_select)
        sleep(5)
        listener = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                while True:
                    print("Escuchando...")
                    voice = listener.listen(source)
                    rec = listener.recognize_google(voice)
                    if rec == "Espanol":
                        return "El lenguaje que seleccionaste fue español","es"
                        break
                    elif rec == "English":
                        return "The language you selected was English","en"
                        break
                    
        except:
            pass
