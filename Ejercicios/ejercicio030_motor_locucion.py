from gtts import gTTS
import os

def narrar(texto):
    language = 'en'
    myobj = gTTS(text=texto, lang=language, slow=False)
    myobj.save("texto.mp3")
    os.system("start texto.mp3")