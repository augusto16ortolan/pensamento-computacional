import pyttsx3

#Inicializa o mecanismo TTS
engine = pyttsx3.init()

#Informa o texto que queira falar
texto = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged"
engine.setProperty('volume', 1)
engine.setProperty('rate', 200) #padrao é 200

voices = engine.getProperty('voices') 
print(voices[0].name)
print(voices[1].name)

engine.setProperty('voice', voices[1].id) 

#Fala o texto
engine.say(texto)

#Aguarda até que a fala seja concluída antes de encerrar o programa
engine.runAndWait()