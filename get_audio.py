# Aqui se encontrarán las clases que transformarán el texto a un audio
# formato del audio --> mp3

# Librerias externas
import openai
import pyttsx3
from pydub import AudioSegment
from abc import ABC, abstractmethod
from dotenv import load_dotenv
import os

# carga .env
load_dotenv()

# configuracion de la API key
openai.api_key = os.getenv("OPENAI_API_KEY")


# clase padre
class AudioGeneretor(ABC):

    @abstractmethod
    def generate_audio(self):
        pass


# Generar de manera offline un audio mp3
# input
# --> texto
# --> file_wav = nombre del archivo .wav que genera (audio.wav defaul)
# --> file_mp3 = nombre del audio final que genera (audio.mp3 defaul)
# --> language = idioma del audio (en(ingles) defaul)
# --> speed = velocidad de reproduccion (150 defaul)
class AudioGeneretorOffline(AudioGeneretor):
    
    def generate_audio(self ,text:str ,file_wav="audio.wav",file_mp3="audio.mp3",language="en"):
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

        # Generar archivo WAV temporal
        engine.save_to_file(text, file_wav)
        engine.runAndWait()

        # Convertir WAV → MP3 con pydub
        sonido = AudioSegment.from_wav(file_wav)
        sonido.export(file_mp3, format="mp3")


# Genera un audio mp3 desde un texto
# Input
# --> text (str) = texto que se genera a audio
# --> voice (alloy defaul) = voz del audio
# --> file_mp3 (audio.mp3 defaul) = nombre del audio
class AudioGeneretorOnline(AudioGeneretor):
    
    def generate_audio(self, text:str, voice="alloy", file_mp3="audio.mp3"):
        
        # Generar audio con OpenAI TTS
        respuesta = openai.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice=voice,
            input=text
        )

        # Guardar el audio directamente
        with open(file_mp3, "wb") as f:
            f.write(respuesta.audio)