from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json
from pygame import mixer
from time import sleep

def get_page():
    req = Request("https://downdetector.com/status/td-ameritrade")
    req.add_header( 'User-Agent', 'pluthus algo trade')

    content = urlopen(req)
    soup = BeautifulSoup(content,'html.parser')
    status = str(soup.find('div', class_='entry-title').string)
    if status.strip() == 'Problems at TD Ameritrade':
        make_alert()

def make_alert():
    mixer.init()
    mixer.music.load('Napalm_Death_You_Suffer.wav')
    mixer.music.play()
   


if __name__=='__main__':
    while True:
        print("running")
        get_page()
        print('waiting')
        sleep(120)