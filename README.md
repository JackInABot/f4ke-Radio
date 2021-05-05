# F4ke Radio 
A local MP3 player that simulates a radio

## What is it?  
This program is an mp3 player which is designed to allow the user to implement custom radio elements to make the audio seem like it's a real radio show. It is highly modular and completely up to the user how realistic it sounds. With a simple directory-driven approach the user can just add a folder with their own choice of mp3s and create a localised fake radio station.

## What's the point of it?  
This is to simulate a real radio device which tunes into radio stations but implemented locally. There are 24/7 radio’s on YouTube and they are typically very good, but I found myself spending a lot of time searching for the right one. I love the atmosphere, but don’t like the reliance of internet and when they shut down, I need to find a new one. This way I always have radio stations saved on my machine. Additionally I am also a music snob and so I wanted a solution that enabled me to create lots of these 24/7 radios with all the music that I love without losing the atmosphere of a nice relaxing 24/7 radio show.  

TLDR: It’s meant to be used as a tool to simulate a relaxing radio show playing in the background while you have your attention elsewhere. 

## Installation
Download via git with:
`git clone https://github.com/JackInABot/f4ke-Radio.git`

you can also download the condensed files and extract into your desired directory

## Running
Only tested and run on Windows. Linux users are welcome to try and run this, if there are any issues I suspect if you are a linux user you're probably more than capable of fixing the linux speific issue yourself. I'll see if i can test it a least and _maybe_ add linux support in the future. No promeses though.

You'll need to install Python 3 if you havnt already.
after you've installed python 3 you'll need to install the following if you havnt already:
- `pip3 install pygame`
- `pip3 install mutagen.mp3`


## How do I use it?  
Okay, here’s a quick rundown.  

### Running the program  
RUN `main.py` just double click that $#!T 

Create a shortcut if you want and place it on your desktop / taskbar 

#### Prerequisites:   
You must have at least one radio show in the `RADIO_STATIONS` directory.  

#### Changing stations  
Click the buttons `next` or `previous` on the UI to change station. This function is also bound the `Left` and `Right` Arrow Keys.  

#### Changing the volume  
Click the `Volume ▲` or `Volume ▼` buttons on the UI to change the volume by a value of 0.2 each click. These functions are also bound to the `Up` and `Down` Arrow Keys. And also by scrolling your mouse wheel (if you have one) up and down you can change the volume up and down.

### Creating a new radio station  
Go to the `RADIO_STATIONS` directory and make a new folder. The name of the folders in the `RADIO_STATIONS` directory are the names of the radio stations.

All radio station folders inside `RADIO_STATIONS` directory must have the following inside them:  

- Folder named `HostAfterBreak`  
- Folder named `HostBeforeBreak`  
- Folder named `Tracks`  

The folders `HostAfterBreak`,`HostBeforeBreak`can be blank.  

The folder `Tracks` needs at least 1 audio file inside.  

More information can be found on the [Wiki](https://github.com/JackInABot/f4ke-Radio/wiki)

### Deleting a radio station 
Just delete the folder inside `RADIO_STATIONS` that you don't want any more or I guess you could just move that folder elsewhere if you're too scared to delete it. 

### Editing a radio station 
Drop music into the `Tracks` folder. If you have duplicate names for the files add a number in brackets e.g. `example.mp3 (1) example.mp3 (2)` and the radio will know to take that part away when displaying the tracks in the UI.

Add audio you want to play before an ad break in the `HostBeforeBreak` folder. Just drop it right in there. 

Add audio you want to play after an ad break in the `HostAfterBreak` folder. Just drop it right in there. 

There is more stuff like explaining how to use the radio cheats menu, how to set up station-settings and how to make these radio stations sound as realistic as possible in the  [Wiki](https://github.com/JackInABot/f4ke-Radio/wiki) 
