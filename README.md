# F4ke Radio
## What is it? 

This program is an mp3 player which is designed to allow the user to implement custom radio elements to make the audio seem likes it's a radio show. It is highly modular and completely up to the user how realistic it sounds. With a simple directory-driven approch the user can just ad a folder with theior own choise to mp3s and create a localised fake radio station.

## What's the point of this? 

I wanted to make something to help with my loneliness. There are 24/7 radio’s on YouTube and it is typically very cosy, and I love the atmosphere of them. But I am also a music snob and so I wanted a solution that enabled me to create lots of these 24/7 radios with all the music that I love without losing the atmosphere of a nice relaxing 24/7 radio show. 

TLDR: It’s meant to be used as a tool to simulate a relaxing radio show playing in the background while you have your attention elsewhere. It’s all about the atmosphere. 

## How do I use it? 

Okay I’ll run you through how to do everything. 

### Running the program 

RUN `main.py` just double click that $#!T
Create a shortcut if you want and place it on your dasktop / taskbar

#### Prerequisites:  

You must have at least one radio show in the `RADIO_STATIONS` directory. 

#### Changing stations 

Click the buttons `next` or `previous` on the UI to change station. This function is also bound the `Left` and `Right` Arrow Keys. 

#### Changing the volume 

Click the `Volume ▲` or `Volume ▼` buttons on the UI to change the volume by a value of 0.2 each click. This functions is also bound to the `Up` and `Down` Arrow Keys. 

 

 

### Creating a new radio station 

Go to the `RADIO_STATIONS` directory and make a new folder. The name of the folders in the `RADIO_STATIONS` directory are the names of the radio stations. 

All radio station folders inside `RADIO_STATIONS` directory must have the following inside them: 

- Folder named `HostAfterBreak` 
- Folder named `HostBeforeBreak` 
- Folder named `Tracks` 
- File named `settings.json` 

The folders `HostAfterBreak`,`HostBeforeBreak`can be blank. 
The folder `Tracks` needs at least 1 mp3 file inside. 
The file `settings.json` needs to have appropriate settings inside like so: 
`{
    "TracksSectionSize":4, 
    "AdsSectionSize":0, 
    "IncludeAdBreaks": false 
}`

### Deleting a radio station
Just delete the folder inside `RADIO_STATIONS` that you dont want anymore or I guess you could just move that folder elsewhere if you're too scared to delete it
