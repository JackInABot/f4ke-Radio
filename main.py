import os
from os.path import normpath, basename
import pygame
import tkinter as tk
import webbrowser

import DirectoryHelper as directoryHelper
import SettingsHelper as settingsHelper
import StringHelper as stringHelper

#MAIN
pygame.init() #turn all of pygame on.
os.getcwd()

#VARS
STATIONS = []
RADIO_ELEMENT_LIST = []
CURRENT_ELEMENT = 0
CURRENT_STATION = 0
Just_Tuned_In = True

#SETTINGS VARS (these can be edited to suit user preference using <prefix>-settings.json files)
#global-radio-settings
CURRENT_VOLUME = 0 #Volume of the radio
RADIO_STATIONS_DIR = "" #Directory
#station-settings
TracksSectionSize = 0 #How many tracks play until an ad break
AdsSectionSize = 0 #How many ads play until return to tracks
IncludeAdBreaks = True #if station includes ad breaks

# Functions
def VolumeUp():
    global CURRENT_VOLUME
    if(CURRENT_VOLUME < 0.99):
        CURRENT_VOLUME = CURRENT_VOLUME + 0.02
        pygame.mixer.music.set_volume(CURRENT_VOLUME)
        UpdateVolumeLabel(CURRENT_VOLUME)

def VolumeDown():
    global CURRENT_VOLUME
    if(CURRENT_VOLUME > 0.01):
        CURRENT_VOLUME = CURRENT_VOLUME - 0.02
        pygame.mixer.music.set_volume(CURRENT_VOLUME)
        UpdateVolumeLabel(CURRENT_VOLUME)

def HyperjumpToReadMe():
    webbrowser.open('https://github.com/JackInABot/f4ke-Radio#readme')

def HyperjumpToWiki():
    webbrowser.open('https://github.com/JackInABot/f4ke-Radio/wiki')

def SkipForwardOneTrack():
    directoryHelper.stopRadioStationTracks()
    _playRadioStation()

def SkipBackwardsOneTrack():
    global CURRENT_ELEMENT
    directoryHelper.stopRadioStationTracks()
    CURRENT_ELEMENT -=2
    _playRadioStation()

def Init():
    global STATIONS
    #on init, load the global settings
    _applyGlobalRadioSettings()
    #set the radio list
    STATIONS = directoryHelper.getRadioStations(RADIO_STATIONS_DIR)
    #on startup we play the first station in the list
    UpdateStationLabel(STATIONS[CURRENT_STATION])
    _applyStationSettings(STATIONS[CURRENT_STATION])
    _assembleRadioElements(0)
    _playRadioStation()

def NextStation():
    global CURRENT_STATION
    new_station_id = CURRENT_STATION + 1
    #check if last in list
    stations_len = len(STATIONS)
    if new_station_id == stations_len:
        new_station_id = 0 #wrap around to first

    #init the new station
    _setupNewStation(new_station_id)

def PreviousStation():
    global CURRENT_STATION
    new_station_id = CURRENT_STATION - 1
    #check if last in list
    stations_len = len(STATIONS)
    if new_station_id == -1:
        new_station_id = stations_len - 1 #jump to end

    #init the new station
    _setupNewStation(new_station_id)

########################################### Private Functions ###########################################
def _setupNewStation(new_station_id):
    _updateCurrentStation(new_station_id)
    _unloadLastStation()
    _applyStationSettings(STATIONS[new_station_id])

    UpdateStationLabel(STATIONS[new_station_id])

    _assembleRadioElements(new_station_id)
    _playRadioStation()

def _assembleRadioElements(stationId):
    global RADIO_ELEMENT_LIST, CURRENT_ELEMENT
    station_dir = os.path.join(RADIO_STATIONS_DIR, STATIONS[stationId])
    scrambleList = True
    #get and assemble track paths
    station_tracks_list = stringHelper.AssembleRadioElements(station_dir, directoryHelper.STATION_TRACKS_FOLDER, scrambleList)
    #get and assemble ad paths
    station_ads_list = stringHelper.GetAdverts(scrambleList)
    #get and assemble Host Before Break talk
    station_HostBeforeBreak_list = stringHelper.AssembleRadioElements(station_dir, directoryHelper.STATION_HOST_BEFORE_BREAK_FOLDER, scrambleList)
    #get and assemble Host After Break talk
    station_HostAfterBreak_list = stringHelper.AssembleRadioElements(station_dir, directoryHelper.STATION_HOST_AFTER_BREAK_FOLDER, scrambleList)
    #mix up the radio station elements if applicable
    RADIO_ELEMENT_LIST = stringHelper.MixRadioElements(station_tracks_list, station_ads_list, station_HostBeforeBreak_list, station_HostAfterBreak_list, TracksSectionSize, AdsSectionSize, IncludeAdBreaks)
    #randomize where in the list we are
    CURRENT_ELEMENT = stringHelper.RandomizeNumber(len(RADIO_ELEMENT_LIST) -1)


def _playRadioStation():
    global CURRENT_ELEMENT, Just_Tuned_In
    pos = pygame.mixer.music.get_pos()
    if int(pos) == -1:
        #if we reach the end of the list, wrap around and restart
        if(CURRENT_ELEMENT == len(RADIO_ELEMENT_LIST)): CURRENT_ELEMENT = 0
        #if user rewinds track on first element in list, we wrap to the end element
        if(CURRENT_ELEMENT < 0): CURRENT_ELEMENT = len(RADIO_ELEMENT_LIST) - 1

        if(Just_Tuned_In):
            #if we just tuned in, we simulate the element having played a bit before joining
            current_element_length = stringHelper.GetElementLength(RADIO_ELEMENT_LIST[CURRENT_ELEMENT])
            start_position = stringHelper.RandomizeFloat(current_element_length)
            pygame.mixer.music.load(RADIO_ELEMENT_LIST[CURRENT_ELEMENT])
            pygame.mixer.music.play(0, start_position)
            CURRENT_ELEMENT += 1
            Just_Tuned_In = False
        else:
            pygame.mixer.music.load(RADIO_ELEMENT_LIST[CURRENT_ELEMENT])
            pygame.mixer.music.play()
            CURRENT_ELEMENT += 1

    #update track label
    if(CURRENT_ELEMENT == 0):
        UpdateRadioElementLabel(RADIO_ELEMENT_LIST[CURRENT_ELEMENT])
    else: #CURRENT_ELEMENT += 1 main loop steps one up
        UpdateRadioElementLabel(RADIO_ELEMENT_LIST[CURRENT_ELEMENT -1])

    root.after(200, _playRadioStation)

def _unloadLastStation():
    global RADIO_ELEMENT_LIST, CURRENT_ELEMENT
    RADIO_ELEMENT_LIST = []
    CURRENT_ELEMENT = 0
    directoryHelper.stopRadioStationTracks()

def _updateCurrentStation(newId):
    global CURRENT_STATION
    CURRENT_STATION = newId

def _applyStationSettings(stationDir):
    global TracksSectionSize, AdsSectionSize, IncludeAdBreaks, Just_Tuned_In
    settings = settingsHelper.GetStationSettings(RADIO_STATIONS_DIR, stationDir)
    TracksSectionSize = settings['TracksSectionSize']
    AdsSectionSize = settings['AdsSectionSize']
    IncludeAdBreaks = settings['IncludeAdBreaks']
    UpdateVolumeLabel(CURRENT_VOLUME)
    Just_Tuned_In = True

def _applyGlobalRadioSettings():
    global CURRENT_VOLUME, RADIO_STATIONS_DIR
    settings = settingsHelper.GetGlobalRadioSettings()
    CURRENT_VOLUME = settings['RadioVolumeStartValue']
    RADIO_STATIONS_DIR = settings['RadioStationsDirectory']

def VolumeUpEvent(event):
    VolumeUp()
def VolumeDownEvent(event):
    VolumeDown()
def NextStationEvent(event):
    NextStation()
def PreviousStationEvent(event):
    PreviousStation()
def MouseWheelVolumeEvent(event):
    if event.num == 5 or event.delta == -120:
        VolumeDown()
    if event.num == 4 or event.delta == 120:
        VolumeUp()

########################################### UI STUFF ###########################################
def UpdateStationLabel(newStationValue):
    stationLabel['text'] = stringHelper.GetStationNameFromStationString(newStationValue)
    frequencyLabel['text'] = stringHelper.GetFrequencyFromStationString(newStationValue)

def UpdateVolumeLabel(newVolumeValue):
    percentageValue = "{:.0%}".format(newVolumeValue)
    volumeLevelLabel['text'] = percentageValue

#we have to expect a full directory for this so string manipulation needed
def UpdateRadioElementLabel(elementDir):
    elementName = basename(normpath(elementDir))
    if (stringHelper.isDuplicate(elementDir)): elementName = elementName.split('(')[0]
    if 'mp3' in elementName or 'flac' in elementName or 'wav' in elementName: elementName = os.path.splitext(elementName)[0]
    elementLabel['text'] = elementName

# MAIN LOOP
root = tk.Tk()
frame = tk.Frame(root)

#LABELS
stub1 = tk.Label(root, text="")
frequencyLabel = tk.Label(root, text="frequency", font=("Calibri", 11))
stationLabel = tk.Label(root, text="Station", font=("Impact", 30))
elementLabel = tk.Label(root, text="Track", font=("Calibri", 11))
volumeLevelLabel = tk.Label(root, text="Volume", font=("Calibri", 9))

#BUTTONS
previousStationButton = tk.Button(root, text="⯇ Previous", command=PreviousStation, height = 5, width = 10, borderwidth = '4')
nextStationButton = tk.Button(root, text="Next ⯈", command=NextStation, height = 5, width = 10, borderwidth = '4')
volumeUpButton = tk.Button(root, text="Volume ▲", command=VolumeUp, height = 1, width = 10)
volumeDownButton = tk.Button(root, text="Volume ▼", command=VolumeDown, height = 1, width = 10)

root.bind('<Left>', PreviousStationEvent)
root.bind('<Right>', NextStationEvent)
root.bind('<Up>', VolumeUpEvent)
root.bind('<Down>', VolumeDownEvent)

root.bind("<MouseWheel>", MouseWheelVolumeEvent)

#MENU
menuBar = tk.Menu(root)

# Create a pull-down menu for file operations
cheatMenu = tk.Menu(menuBar, tearoff = False)
cheatMenu.add_command(label = "Forward 1 Track", command = SkipForwardOneTrack)
cheatMenu.add_command(label = "Rewind 1 Track", command = SkipBackwardsOneTrack)
menuBar.add_cascade(menu = cheatMenu, label = "Cheats")

# Create a pull-down menu for help operations
helpMenu = tk.Menu(menuBar, tearoff = False)
helpMenu.add_command(label = "Go to Read Me", command = HyperjumpToReadMe)
helpMenu.add_command(label = "Go to Wiki", command = HyperjumpToWiki)
menuBar.add_cascade(menu = helpMenu, label = "Help")
root.config(menu=menuBar)

stub1.pack(side=tk.TOP)

stationLabel.pack(side=tk.TOP)
frequencyLabel.pack(side=tk.TOP)
elementLabel.pack(side=tk.TOP)

previousStationButton.pack(side=tk.LEFT)
nextStationButton.pack(side=tk.RIGHT)

volumeDownButton.pack(side=tk.BOTTOM)
volumeLevelLabel.pack(side=tk.BOTTOM)
volumeUpButton.pack(side=tk.BOTTOM)

root.geometry("500x200")

Init()
root.mainloop()
