import json
import os
import DirectoryHelper as directoryHelper

DefaultTracksSectionSize = 4 #How many tracks play until an ad break
DefaultAdsSectionSize = 2 #How many ads play until return to tracks
DefaultIncludeAdBreaks = True #if station includes ad breaks

def GetSettings(stationFolder):
    pathToSettings = os.path.join(directoryHelper.RADIO_STATIONS_FOLDER, os.path.join(stationFolder, 'station-settings.json'))
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