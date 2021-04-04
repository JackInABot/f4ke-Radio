import json
import os
import DirectoryHelper as directoryHelper

def GetSettings(stationFolder):
    pathToSettings = os.path.join(directoryHelper.RADIO_STATIONS_FOLDER, os.path.join(stationFolder, 'settings.json'))
    stationSettings = []
    with open(pathToSettings) as myfile:
        data=myfile.read()
        # parse file
        obj = json.loads(data)
        # show values
        stationSettings.append(obj['TracksSectionSize'])
        stationSettings.append(obj['AdsSectionSize'])
        stationSettings.append(obj['IncludeAdBreaks'])

    return stationSettings