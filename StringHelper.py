import os
import re
import random
from mutagen.mp3 import MP3
from mutagen.wave import WAVE
from mutagen.flac import FLAC

import DirectoryHelper as directoryHelper

def RandomizeNumber(maxValue):
    return random.randint(0, maxValue)

def RandomizeFloat(maxValue):
    return random.uniform(0, maxValue)

def GetAdverts(scrambleList = False):
    ads = directoryHelper.getRadioStationAdBreaks()

    station_element_list = []
    for ad in ads:
        station_element_list.append(os.path.join(directoryHelper.RADIO_ADVERTS_FOLDER, ad))
    if(scrambleList == True): station_element_list = scramble(station_element_list)
    return station_element_list

def AssembleRadioElements(station_dir, radio_elements_dir, scrambleList = False):
    #get the correct elements from the correct folder using radio_elements_dir
    elements = []
    if(radio_elements_dir == directoryHelper.STATION_TRACKS_FOLDER): elements = directoryHelper.getRadioStationTracks(station_dir)
    if(radio_elements_dir == directoryHelper.STATION_HOST_BEFORE_BREAK_FOLDER): elements = directoryHelper.getRadioStationHostBeforeBreaks(station_dir)
    if(radio_elements_dir == directoryHelper.STATION_HOST_AFTER_BREAK_FOLDER): elements = directoryHelper.getRadioStationHostAfterBreaks(station_dir)

    station_elements_dir = os.path.join(station_dir, radio_elements_dir)
    station_element_list = []
    for element in elements:
        station_element_list.append(os.path.join(station_elements_dir, element))
    if(scrambleList == True): station_element_list = scramble(station_element_list)
    return station_element_list

def scramble(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest

def isDuplicate(s):
    return bool(re.search(r'\(\d+\)', s))

def GetElementLength(radioElement):
    filename, file_extension = os.path.splitext(radioElement)
    if(file_extension == ".mp3"):
        audio = MP3(radioElement)
        return audio.info.length
    if(file_extension == ".flac"):
        audio = FLAC(radioElement)
        return audio.info.length
    if(file_extension == ".wav"):
        audio = WAVE(radioElement)
        return audio.info.length
    #unsupported format
    return 0

def MixRadioElements(tracks, ads, hostBeforeBreak, hostAfterBreak, TracksSectionSize, AdsSectionSize, IncludeAdBreaks):
    #VARS
    station_mixed_list = []

    temp_ads_list = ads.copy()
    temp_hostBeforeBreak_list = hostBeforeBreak.copy()
    temp_hostAfterBreak_list = hostAfterBreak.copy()

    while tracks:
        #add the number of tracks
        for i in range(0, TracksSectionSize):
            if (len(tracks) == 1):
                station_mixed_list.append(tracks[0])
                tracks.remove(tracks[0])
            elif (TracksSectionSize > len(tracks)):
                for track in tracks:
                    station_mixed_list.append(track)
                    tracks.remove(track)
            else:
                station_mixed_list.append(tracks[i])
                tracks.remove(tracks[i])
            if not tracks:
                break
        
        if(IncludeAdBreaks):
            #add host talk before ad break
            if not temp_hostBeforeBreak_list: temp_hostBeforeBreak_list = hostBeforeBreak.copy()
            if temp_hostBeforeBreak_list: #this enables folders to be empty if needed
                station_mixed_list.append(temp_hostBeforeBreak_list[0])
                temp_hostBeforeBreak_list.remove(temp_hostBeforeBreak_list[0])
            #add the list ads
            if temp_ads_list: #this enables folders to be empty
                for i in range(0, AdsSectionSize):
                    station_mixed_list.append(temp_ads_list[0])
                    #if(len(temp_ads_list) == 1):
                    temp_ads_list.remove(temp_ads_list[0])
                    # else:
                    #     temp_ads_list.remove(temp_ads_list[i])
                    if not temp_ads_list: temp_ads_list = ads.copy() #if temp ads is empty, replenish it
            #add host talk after ad break
            if not temp_hostAfterBreak_list: temp_hostAfterBreak_list = hostAfterBreak.copy()
            if temp_hostAfterBreak_list: #this enables folders to be empty
                station_mixed_list.append(temp_hostAfterBreak_list[0])
                temp_hostAfterBreak_list.remove(temp_hostAfterBreak_list[0])

    return station_mixed_list