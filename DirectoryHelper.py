import os
from mutagen.mp3 import MP3
import pygame

from os import listdir
from os.path import isdir, isfile, join

#CONSTANTS
RADIO_STATIONS_FOLDER = "RADIO_STATIONS"
RADIO_ADVERTS_FOLDER = "ADVERTS"
STATION_TRACKS_FOLDER = "Tracks"
STATION_ADS_FOLDER = "Ads"
STATION_HOST_BEFORE_BREAK_FOLDER = "HostBeforeBreak"
STATION_HOST_AFTER_BREAK_FOLDER = "HostAfterBreak"


def getRadioStations(radioStationsDir):
    onlyfolders = [f for f in listdir(radioStationsDir) if isdir(join(radioStationsDir, f))]
    return onlyfolders

def getRadioStationTracks(radioStationDir):
    onlyfiles = [f for f in listdir(os.path.join(radioStationDir,STATION_TRACKS_FOLDER)) if isfile(join(os.path.join(radioStationDir,STATION_TRACKS_FOLDER), f))]
    return onlyfiles

def getRadioStationAdBreaks():
    onlyfiles = [f for f in listdir(RADIO_ADVERTS_FOLDER) if isfile(join(RADIO_ADVERTS_FOLDER, f))]
    return onlyfiles

def getRadioStationHostBeforeBreaks(radioStationDir):
    onlyfiles = [f for f in listdir(os.path.join(radioStationDir,STATION_HOST_BEFORE_BREAK_FOLDER)) if isfile(join(os.path.join(radioStationDir,STATION_HOST_BEFORE_BREAK_FOLDER), f))]
    return onlyfiles

def getRadioStationHostAfterBreaks(radioStationDir):
    onlyfiles = [f for f in listdir(os.path.join(radioStationDir,STATION_HOST_AFTER_BREAK_FOLDER)) if isfile(join(os.path.join(radioStationDir,STATION_HOST_AFTER_BREAK_FOLDER), f))]
    return onlyfiles

def getFileLength(filePath):
    audio = MP3(filePath)
    audio_info = audio.info
    length_in_secs = int(audio_info.length)
    return length_in_secs

def playRadioStationElement(elementDir):
    pygame.mixer.music.load (elementDir)  # Get the first track from the playlist
    pygame.mixer.music.play() # Play the music

def startRadioStation(root, mixedList):
    stationList = [] #example: "/station/Tracks/example.mp3"
    stationList = mixedList

    for i in range(len(stationList)):
        pygame.mixer.music.load ( stationList[i] )  # Get the first track from the playlist
        pygame.mixer.music.set_endevent ( pygame.USEREVENT )    # Setup the end track event
        pygame.mixer.music.play() # Play the music


        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:    # A track has ended
                stationList.remove(stationList[i])

        root.after(100, startRadioStation(root, mixedList))



            
def stopRadioStationTracks():
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()