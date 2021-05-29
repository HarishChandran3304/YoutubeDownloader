#IMPROTS
from __future__ import unicode_literals
import eel
from pytube import YouTube


#SETUP
eel.init("src")


#HELPER FUNCITONS
@eel.expose
def download(url):
    vid = YouTube(url).streams.get_highest_resolution()
    vid.download()


#MAIN
def main():
    eel.start("index.html", size=(1280, 720))


#MAIN CALL
if __name__ == "__main__":
    main()