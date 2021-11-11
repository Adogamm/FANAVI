class EnglishAssistant:
    
    def presentacion():
        listener = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                while True:
                    print("Escuchando...")
                    voice = listener.listen(source)
                    rec = listener.recognize_google(voice)
                    print(rec)
                    if rec == "quien Eres":
                        voice_string = "¡Hola!, yo seré tu pequeño asistente virtual"
                        assistant_voice.voice_assistant(voice_string)
                        sleep(5)
                    elif rec == "adios":
                        voice_string = "Hasta luego"
                        assistant_voice.voice_assistant(voice_string)
                        break
                    else:
                        voice_string = "Lo siento, no entendí"
                        assistant_voice.voice_assistant(voice_string)
        except:
            passs