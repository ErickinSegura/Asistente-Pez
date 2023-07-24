import speech_recognition as sr
import pygame

r = sr.Recognizer()
pygame.init()
pygame.mixer.init()

listen = pygame.mixer.Sound("./resources/listening.wav")  
generate = pygame.mixer.Sound("./resources/generating.wav")
generate.set_volume(10)
error = pygame.mixer.Sound("./resources/error.wav")


class Listener:
    def listen():
        with sr.Microphone() as source:
              
            print("Diga algo:")
            listen.play()
            audio = r.listen(source)
            print("Reconociendo...")
            try:
                audio_text = r.recognize_google(audio, language='es-ES')
                print("Texto: {}".format(audio_text))
                generate.play()
                return audio_text.lower()
            except:
                print("Lo siento, no te entiendo")
                error.play()

