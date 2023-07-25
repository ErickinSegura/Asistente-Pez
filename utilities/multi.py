from modules.talk import Talker

from youtubesearchpython import VideosSearch
import pywhatkit
from datetime import datetime


talker = Talker()

#Utilidades

def play(res):
    music = res.replace('reproduce', '')
    music = res.replace('pon', '')
    videosSearch = ((VideosSearch(music+" audio", limit = 1)).result())['result'][0]['title']
    print("Reproduciendo " + videosSearch + " en YouTube")
    talker.talk("Reproduciendo " + videosSearch+ " en YouTube")
    pywhatkit.playonyt(videosSearch+" audio")

def search_on_google(res):
    pywhatkit.search((res.replace('BUSCA', '')).lower())

def hora(res):
    hora = datetime.datetime.now().strftime("%H:%M")
    print("Son las " + hora)
    talker.talk("Son las " + hora)

def fecha(res):
    fecha = datetime.today().strftime("%d/%m/%Y")
    print("Hoy es " + fecha)
    talker.talk("Hoy es " + fecha)

#Easter Eggs

def feliz(res):
    talker.talk("Al toque mi rey")
    pywhatkit.playonyt("Fish dance Beach Parade but is Chiptune")

def cumbia(res):
    talker.talk("A darle barrio, sin miedo pero con clase")
    pywhatkit.playonyt("Mix de cumbias altamente sofisticadas para gente sofisticada")
    
def test(res):
    talker.talk("test")
