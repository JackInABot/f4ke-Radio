import json
import os
import DirectoryHelper as directoryHelper

#global radio settings default values
DefaultRadioVolumeStartValue = 0.7 #default start value of volume set to 70%
DefaultRadioStationsFolder = "RADIO_STATIONS" #default place where the radio stations are (in the current directory)

#stations settings default values
DefaultTracksSectionSize = 4 #How many tracks play until an ad break
DefaultAdsSectionSize = 2 #How many ads play until return to tracks
DefaultIncludeAdBreaks = True #if station includes ad breaks

#GLOBAL SETTINGS
def GetGlobalRadioSettings():
    pathToSettings = os.path.join(directoryHelper.GLOBAL_RADIO_SETTINGS)
    globalSettings = {}
    if(os.path.isfile(pathToSettings)):
        with open(pathToSettings) as myfile:
            data=myfile.read()
            # parse file
            obj = json.loads(data)
            # save valus to dictionary
            try: globalSettings['RadioVolumeStartValue'] = obj['RadioVolumeStartValue']
            except: _setDefaultRadioVolumeValue(globalSettings)

            try: globalSettings['RadioStationsDirectory'] = obj['RadioStationsDirectory']
            except: _setDefaultRadioStationsFolder(globalSettings)

    return globalSettings

def _setDefaultRadioVolumeValue(globalSettings):
    globalSettings['RadioVolumeStartValue'] = DefaultRadioVolumeStartValue

def _setDefaultRadioStationsFolder(globalSettings):
    globalSettings['RadioStationsDirectory'] = DefaultRadioStationsFolder

def GetStationSettings(radioStationsDir, stationFolder):
    pathToSettings = os.path.join(radioStationsDir, os.path.join(stationFolder, 'station-settings.json'))
    stationSettings = {}
    if(os.path.isfile(pathToSettings)):
        with open(pathToSettings) as myfile:
            data=myfile.read()
            # parse file
            obj = json.loads(data)
            # save valus to dictionary
            try: stationSettings['TracksSectionSize'] = obj['TracksSectionSize']
            except: _setDefaultTracksSectionSize(stationSettings)

            try: stationSettings['AdsSectionSize'] = obj['AdsSectionSize']
            except: _setDefaultAdsSectionSize(stationSettings)

            try: stationSettings['IncludeAdBreaks'] = obj['IncludeAdBreaks']
            except: _setDefaultIncludeAdBreaks(stationSettings)
    else:
        _setDefaultTracksSectionSize(stationSettings)
        _setDefaultAdsSectionSize(stationSettings)
        _setDefaultIncludeAdBreaks(stationSettings)

    return stationSettings


def _setDefaultTracksSectionSize(stationSettings):
    stationSettings['TracksSectionSize'] = DefaultTracksSectionSize

def _setDefaultAdsSectionSize(stationSettings):
    stationSettings['AdsSectionSize'] = DefaultAdsSectionSize

def _setDefaultIncludeAdBreaks(stationSettings):
    stationSettings['IncludeAdBreaks'] = DefaultIncludeAdBreaks