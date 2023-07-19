from modules.talk import Talker
import pywhatkit

talker = Talker()

def play(res):
    music = res.replace('REPRODUCE', '')
    print("Reproduciendo" + music.lower())
    talker.talk("Reproduciendo " + music)
    pywhatkit.playonyt(music)

def search_on_google(res):
    pywhatkit.search((res.replace('BUSCA', '')).lower())
