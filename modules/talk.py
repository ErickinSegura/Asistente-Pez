import os
import pygame

voice = 'es-MX-JorgeNeural'
class Talker:
    def talk(self, res):
        command = f'edge-tts --voice "{voice}" --text "{res}" --write-media "data.mp3"'
        os.system(command)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("data.mp3")

        try:
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as e:
            print(e)
        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            os.remove('data.mp3')
    

