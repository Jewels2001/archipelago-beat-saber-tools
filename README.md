# archipelago-beat-saber-tools



## song_scraper.py
This program scrapes the song files from a zip (as exported from BSManager) and generates a portion of the yaml (`songs`) to be pasted into your archipelago yaml

For versions 0.0.5 and 0.1.0 of [Beat Saber Archipelago](https://github.com/CurrentlyPending/BeatSaberAP)

Works from wherever you have a list of songs 
- can export to zip, extract, and run this script from that folder
- can plop this script into your /Beat Saber_Data/CustomLevels folder and run it from there (however I don't recommend leaving the script in there afterwards when you run the game.. it theory it might not affect anything but who knows what the game will do when it sees a random file inside its folder)


### steps:
currently you need to: 
- **have your songs/maps already downloaded** 
(ie, in BSManager, if you have a playlist, download the songs from them/ click "synchronize playlist" so that they appear in the maps menu)
Then click *Export Maps* so that a `.zip` file is generated containing all of the beatmaps/songs. The playlist/.bplist file will **NOT** currently work because it does not contain all of the information needed (the yaml needs the song levelID from beatsaver)


