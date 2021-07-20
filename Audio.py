from gtts import gTTS

from playsound import playsound
audio= 'Anton.mp3'
language= 'es'

sp=gTTS(text= "Hola padre, yo soy ANTON", lang= language, slow=False)

sp.save(audio)
playsound(audio)