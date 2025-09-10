# Aqui se encontrarán las clases que transformarán el texto a un audio
# formato del audio --> mp3

# Librerias externas 
import pyttsx3
from pydub import AudioSegment
from abc import ABC, abstractmethod


# clase padre
class AudioGeneretor(ABC):

    @abstractmethod
    def generate_audio(self):
        pass


# Generar de manera offline un audio wav3
# input --> texto
# output --> audio.wav
class AudioGeneretorWAV(AudioGeneretor):

    def generate_audio(self ,text:str ,file_out="audio.wav",language="en",speed=150):
        engine = pyttsx3.init()

        # Obtener voces disponibles
        voices = engine.getProperty("voices")

        # Buscar una voz que coincida con el idioma
        found_voice = None
        for v in voices:
        
            if language.lower() in v.id.lower():
                found_voice = v
                break
        
        # Configurar la voz
        engine.setProperty("voice", found_voice.id)
        
        # Configurar velocidad
        engine.setProperty("rate", speed)

        # Guardar a archivo WAV
        engine.save_to_file(text, file_out)

        # Ejecutar el motor
        engine.runAndWait()


class AudioGeneretorOffline(AudioGeneretor):
    
    def generate_audio(self ,text:str ,file_wav="audio.wav",file_mp3="audio.mp3",language="en",speed=150):
        engine = pyttsx3.init()

        # Obtener voces disponibles
        voices = engine.getProperty("voices")

        # Buscar una voz que coincida con el idioma
        found_voice = None
        for v in voices:
            
            if language.lower() in v.id.lower():
                found_voice = v
                break

        # Configurar la voz
        engine.setProperty("voice", found_voice.id)
        
        # Configurar velocidad
        engine.setProperty("rate", speed)

        # Generar archivo WAV temporal
        engine.save_to_file(text, file_wav)
        engine.runAndWait()

        # Convertir WAV → MP3 con pydub
        sonido = AudioSegment.from_wav(file_wav)
        sonido.export(file_mp3, format="mp3")



df = AudioGeneretorOffline()
df.generate_audio("hi, how are you? i see you happy, i love it")
