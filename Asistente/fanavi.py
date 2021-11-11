import speech_recognition as sr
from time import sleep
from typing import final
from Text2Speech.text2speech import Text2Speech as t2s

assistant_voice = t2s
launguage_select = "¿Que idioma vas a utilizar, español o ingles?"
final_language = ""

class Assistant:
    def settings():
        assistant_voice.voice_assistant(launguage_select)
        sleep(5)
        listener = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                while True:
                    print("Escuchando...")
                    voice = listener.listen(source)
                    rec = listener.recognize_google(voice)
                    if rec == "español":
                        final_language = "es"
                        return final_language
                        break
                    elif rec == "english":
                        final_language = "en"
                        return final_language
                        break
                    else:
                        break
        except:
            pass

    def functioning():
        listener = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                while True:
                    print("Escuchando...")
                    voice = listener.listen(source)
                    rec = listener.recognize_google(voice)
                    if rec == "hola":
                        voice_string = "¡Hola!, en que puedo ayudarte"
                        assistant_voice.voice_assistant(voice_string)
                    elif rec == "adios":
                        voice_string = "Hasta luego"
                        assistant_voice.voice_assistant(voice_string)
                        break
                    else:
                        voice_string = "Lo siento, no entendí"
                        assistant_voice.voice_assistant(voice_string)
        except:
            pass

prueba = Assistant.settings()
print(final_language)

