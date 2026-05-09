
import yaml
from pathlib import Path

def main():
    """ Scrapes the .zip (or extracted .zip) for all songs"""

    # in future, can just grab straight from songs folder, ie
    # C:\Users\[USERNAME]\BSManager\BSInstances\[Version_Name]\Beat Saber_Data\CustomLevels
    # needs to grab id from song folder
    # -> needs to check if song is default or not

    # then needs to either
    # a) scrape names of available difficulty .dat files
    # or b) scrape data from info.dat
    # could do both to assert that the files exist (and/or know which files to look for)


    # step 1:
    # get path for songs
    # assume you are already in correct folder for now (need a check to make sure later)
    # ie, place script into the folder
    subdirs = [x for x in Path('.').iterdir() if x.is_dir()]
    for cur_dir in subdirs:
        # we have a directory
        # Step 2: extract necessary info (name, levelid, is_official from here)
        # assumes each subdirectory has an info.dat
        # if not, will skip I guess?
        bundle = {
            "name": "",
            "characteristic": "Standard",
            "difficulty": 0,
            "is_official": False,
            "levelid": "13e9"
        }
        # 1 - check if it is a (Built In) song
        #TODO: edge case of song names that contain '-'s (can they contain a - ?)
        #TODO: change all prints to use logging so we can have debug vs info statements (--verbose)
        print(cur_dir)
        dir_name = cur_dir
        # print(type(dir_name))
        # print(type(cur_dir))
        dir_name = str(cur_dir)
        assert type(dir_name) == str, "if this is not string in your version, need to set it (uncomment previous line)"
        
        if "(Built in)" in dir_name:
            #TODO: custom / edge case levelids being different than song names (could hardcode?)
            # do logic here to get song name
            # special ids will need to be processed separately or gathered from elsewhere
            print(f"Processing Built In song: {dir_name}")
            full = dir_name.split("(")[0]
            song_name = full.partition(" - ")[2].strip()
            song_id = song_name.replace(" ", "")
            print(f"Song name: {song_name}")
            print(f"Song id: {song_id}")

            bundle["name"] = song_name
            bundle["is_official"] = True
            bundle["levelid"] = song_id

        else:
            # do logic here to get id and song name 
            print(f"Custom song: {dir_name}")
            song_id = dir_name.split("(")[0].strip()
            print(f"ID: {song_id}")
            song_name_auth = dir_name.split("(", 1)[1].rsplit(")", 1)[0]
            print(f"song name - author: '{song_name_auth}'")
            # this rsplit(,1) or rpartition *should* deal with song names that contain '-'s by taking the last occurrence
            # the spaces should help deal with an author's name too.. 
            # assuming no authors can have spaces / the exact syntax " - " including spaces
            song_name = dir_name.split("(", 1)[1].rpartition(" - ")[0]
            print(f"song name if needed: {song_name}")

            # we use the name with authors because we might have different beat maps be the same song by different authors
            bundle["name"] = song_name_auth
            bundle["levelid"] = song_id

        # now we just need the characteristic and difficulty
        # these can be gathered from the info.dat
        # technically the info.dat lists *all* of the existing characteristics and difficulties
        # any combination of characteristics and difficulties can theoretically exist as far as I know

        # for now we will scrape always standard if exists and the hardest listed difficulty
        # archipelago code only currently allows for 0-4 so we will cap/min the difficulty at/with 4
        # info_dat_path = cur_dir / "Info.dat"
        # print(info_dat_path)
        # print(type(info_dat_path))

        # with open(info_dat_path, 'r') as file:
        #     data = json.load(file)
        

        # we reformat the bundle here and then "ship" it off to the file 
        # so it is saved even if this script breaks half way through running
        yaml_str = reformat_dict_bundle(bundle)

        # with open "a" (append mode) will create a new file if it doesn't exist, 
        # and if it exists, add new content without deleting anything
        # need to ensure dict is properly formatted I guess
        with open("archipelago_beat_saber_songs.yaml", "a", encoding='utf-8') as outf:
            outf.write(yaml_str)

        #breakpoint()

            

    # things to return:
    # - song name
    # - song chracteristic
    # - difficulty (if there are multiple just pick the highest?)
    # - levelid

    pass 


def reformat_dict_bundle(bundle):
    """
    Input: dict
    Output: str formatted correctly as block style yaml
    """
    good_dict = {
        bundle["name"]: {
            "characteristic": bundle["characteristic"],
            "difficulty": bundle["difficulty"],
            "is_official": bundle["is_official"],
            "levelid": bundle["levelid"]
        }
    }
    # add default_style=None to get rid of strings around levelids? not working..
    # currently was outputting any solely numeric ones with '' around them
    # alphanumeric levelids did not have ''
    # might be better to treat as hex or something else? 
    # or maybe it will still work regardless of quotes (one can hope)
    good_yaml_str = yaml.dump(good_dict, allow_unicode=True)
    return good_yaml_str


if __name__ == "__main__":
    main()