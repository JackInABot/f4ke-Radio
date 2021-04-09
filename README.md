# F4ke Radio 

## What is it?  

  

This program is an mp3 player which is designed to allow the user to implement custom radio elements to make the audio seem like it's a real radio show. It is highly modular and completely up to the user how realistic it sounds. With a simple directory-driven approach the user can just ad a folder with their own choice of mp3s and create a localised fake radio station. 

  

## What's the point of it?  

  

This is to simulate a real radio device which tunes into radio stations but implemented locally. There are 24/7 radio’s on YouTube and they are typically very good, but I found myself spending a lot of time searching for the right one. I love the atmosphere, but don’t like the reliance of internet and when they shut down, I need to find a new one. This way I always have radio stations saved on my machine. Additionally I am also a music snob and so I wanted a solution that enabled me to create lots of these 24/7 radios with all the music that I love without losing the atmosphere of a nice relaxing 24/7 radio show.  

  

TLDR: It’s meant to be used as a tool to simulate a relaxing radio show playing in the background while you have your attention elsewhere. 

  

## How do I use it?  

  

Okay, here’s a quick rundown.  

 More in-depth look into everything can be found on the Wiki. 

### Running the program  

  

RUN `main.py` just double click that $#!T 

Create a shortcut if you want and place it on your desktop / taskbar 

  

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

  

The folders `HostAfterBreak`,`HostBeforeBreak`can be blank.  

The folder `Tracks` needs at least 1 audio file inside.  

More information can be found on the Wiki 

### Deleting a radio station 

Just delete the folder inside `RADIO_STATIONS` that you don't want any more or I guess you could just move that folder elsewhere if you're too scared to delete it. 

 

### Editing a radio station 

Drop music into the `Tracks` folder. If you have duplicate names for the files add a number in brackets e.g. `example.mp3 (1) example.mp3 (2)` 

 

Add audio you want to play before an ad break in the `HostBeforeBreak`. Just drop it right in there. 

Add audio you want to play after an ad break in the `HostAfterBreak`. Just drop it right in there. 

 

There is more stuff like the cheats menu and settings that can be found on the Wiki 
