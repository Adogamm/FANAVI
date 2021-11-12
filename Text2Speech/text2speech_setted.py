import os
from gtts import gTTS

class Text2Speech:
    def voice_assistant(voice_string,language):
        if language == "es":
            speech = gTTS(text = str(voice_string), lang = language, slow = False,  tld = "com.mx")
            speech.save("prueba.mp3")
            os.system("start prueba.mp3")
        elif language == "en":
            speech = gTTS(text = str(voice_string), lang = language, slow = False,  tld = "com")
            speech.save("prueba.mp3")
            os.system("start prueba.mp3")