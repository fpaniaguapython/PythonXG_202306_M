#pip install gTTS #Desde una consola del sistema operativo

#Documentación gTTS: https://gtts.readthedocs.io/en/latest/

from gtts import gTTS
import os

mytext = f'Hola María Jesús, ¿qué tal llevas el día?'
language = 'es'
accent = 'es' #'es', 'com.mx', 'us', para el idioma 'es' 
myobj = gTTS(text=mytext, lang=language, tld=accent ,slow=False)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")

#Pedir el nombre al usuario
#Pedir el género (H,M,O)
#Hola, {usuario}, eres y mi amo/a y señor/a