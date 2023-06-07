#pip install gTTS #Desde una consola del sistema operativo

from gtts import gTTS
import os

mytext = f'Hola María Jesús, ¿qué tal llevas el día?'
language = 'es'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")

#Pedir el nombre al usuario
#Pedir el género (H,M,O)
#Hola, {usuario}, eres y mi amo/a y señor/a