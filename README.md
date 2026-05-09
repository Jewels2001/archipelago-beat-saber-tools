# archipelago-beat-saber-tools



## song_scraper.py
This program scrapes the song files from a zip (as exported from BSManager) and generates a portion of the yaml (`songs`) to be pasted into your archipelago yaml

For versions 0.0.5 and 0.1.0 of [Beat Saber Archipelago](https://github.com/CurrentlyPending/BeatSaberAP)
**Note 1:** Custom song lists are only activated by selecting the `preset` gamemode options (ie, `presetaccuracy` or `presetpass`)

***NOTE***: As of May 9, 2026, as discussed on the Archipelago discord in the future-game-design > beat saber channel, version 0.1.0 does not completely work with preset songs so if you are planning on using a custom song list, use world version 0.0.5

Works from wherever you have a list of songs 
- can export to zip, extract, and run this script from that folder
- can plop this script into your /Beat Saber_Data/CustomLevels folder and run it from there (however I don't recommend leaving the script in there afterwards when you run the game.. it theory it might not affect anything but who knows what the game will do when it sees a random file inside its folder. feel free to test and report back though at your own risk)



### how to run (for devs) (see steps for longer explanation)
- `pip install pyyaml`
- run script inside folder containing folders of songs/beatmaps


### steps:
currently you need to: 
- **have your songs/maps already downloaded** 
(ie, in BSManager, if you have a playlist, download the songs from them/ click "synchronize playlist" so that they appear in the maps menu)
Then click *Export Maps* so that a `.zip` file is generated containing all of the beatmaps/songs. The playlist/.bplist file will **NOT** currently work because it does not contain all of the information needed (the yaml needs the song levelID from beatsaver. we could query the API... but scanning the files was easier imo)
- **place this script into folder containing folders of songs/beatmaps**
- **run script using `python song_scraper.py`**
This involves:

    a) installing Python if you don't have it already (you might have it already, open Terminal and run `python --version`)

    b) installing PyYaml so we can output in the correct format `pip install pyyaml`
    c) opening Terminal and running `python song_scraper.py` 
- **copy output into your archipelago options/player yaml under `songs`**
    Make sure the indentation/whitespace is correct, otherwise it won't work!
- **make sure to have chosen one of the `preset` gamemodes in the yaml**
    (set the preset one you want to 50 and ensure the others are 0)
- **as of may 9, 2026, ensure you are using apworld v0.0.5 (there are issues with preset gamemodes in v0.1.0)**

### Other ideas
Ways to integrate with archipelago yaml building:
- this could be implemented on the client or world
- on world side, if preset toggle is chosen, then we could scrape this folder itself and use the songs from there? however does the client also need the list? does it get it from the yaml or can the world send it on creation/connection?

