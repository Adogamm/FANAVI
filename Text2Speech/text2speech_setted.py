import os
from gtts import gTTS

class Text2Speech:
    def voice_assistant(voice_string,language):
        # language = "es"
        # level_domain = "com.mx"
        speech = gTTS(text = str(voice_string), lang = language, slow = False,  tld = "com.mx")
        speech.save("prueba.mp3")
        os.system("start prueba.mp3")