#Import the built-in libraries that don't need to be installed
import os
from zipfile import ZipFile

#Attempt to import the required libraries, and install them if not found
try:
    from moviepy.editor import *
    import pygame
except ImportError:
    os.system('python -m pip install wheel')
    os.system('python -m pip install pygame')
    os.system('python -m pip install moviepy')
    from moviepy.editor import *
    import pygame

#Get absolute path to resource, works for dev and for PyInstaller
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#MUST BE RUN AFTER INITIALIZING PYGAME
def playSong(song):
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

#Function to setup and load the mp4 at pathToFile
def setupClip(pathToFile):
    pygame.init()

    pygame.display.set_caption('You Got Rickrolled!')

    video = VideoFileClip(pathToFile)

    return video

#Main function
def main():
    video = setupClip(resource_path('video.mp4'))
    playSong(resource_path('audio.mp3'))
    video.preview()

    pygame.quit()

    video.close()

#Run the program if the namespace __name__ is __main__
if __name__ == "__main__":
    main()
