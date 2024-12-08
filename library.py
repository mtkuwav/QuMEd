import os
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from typing import Optional
import re



# ========================GLOBAL VARIABLES========================

# Elements specified by the user to get all the categories of the metadata.
ELEMENTS_OF_NAME = {"artist": "%A%",
                    "album": "%a%",
                    "title": "%t%",
                    "track_number": "%n%",
                    "disc_number": "%d%",
                    "bpm": "%b%",
                    "genre": "%g%",
                    "release_date": "%r%"}



# ======================== FILE NAME GETTING FUNCTIONS ========================


def get_file_name (file_path: str):
    """Return the name of the file from the file path in a string.

    Args:
        file_path (str): path of the file.

    Returns:
        string : the name of the file.
    """
    try:
        return os.path.basename(file_path)
    except Exception as e:
        print(f"Uh-Oh ! An error occurred: {e}")
        return ""



def get_files_name(directory_path: str):
    """Return the name of the all the files from the file path in a string.

    Args:
        directory_path (str): path of the directory.

    Returns:
        array: An array of strings, each string being the name of a file in the directory. If an error occurs, an empty array is returned.
    """    
    try:
        return [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    except Exception as e:
        print(f"Uh-Oh ! An error occurred: {e}")
        return []



def get_file_extension (file_name: str):
    """Return the extension of the file from the file name.

    Args:
        file_name (str): name of the file.

    Returns:
        string: the extension of the file.
    """
    extension = ""
    while file_name[-1] != ".":
        extension = file_name[-1] + extension
        file_name = file_name[:-1]
    return extension





# ======================== FILE fFORMAT FUNCTIONS ========================



def get_tags_by_structure(structure: str, file_name: str) -> dict:
    tags = {}
    pattern = structure

    # Replace placeholders with regex patterns
    for key, value in ELEMENTS_OF_NAME.items():
        pattern = pattern.replace(value, f"(?P<{key}>.+?)")

    # Compile the regex pattern
    regex = re.compile(pattern)
    match = regex.match(file_name)

    if match:
        tags = match.groupdict()

        # Convert track number to integer
        if 'track_number' in tags:
            tags['track_number'] = int(tags['track_number'].split(".")[0])

    return tags










"""
edit the metadata of a .flac file.
"""
# I'll might add more parameters later, depending on what the user wants to edit and most importantly, my needs and what mutagen supports.
def edit_mp3_metadata(file_path: str, title: Optional[str] = None, artist: Optional[str] = None, album: Optional[str] = None, bpm: Optional[str] = None, genre: Optional[str] = None, release_date: Optional[str] = None, track_number: Optional[str] = None, disc_number: Optional[str] = None):
    audio = FLAC(file_path)
    audio['title'] = title #modifier pour que le code modifie seulement les arguments qui n'ont pas la valeur none 
    audio['artist'] = artist
    audio['album'] = album
    audio['bpm'] = bpm
    audio['genre'] = genre
    audio.save()

"""
gets an element of the metadata in the file name, based on the separator(s) specified by the user
"""
def get_info(file_name, separators=None):
    return file_name.split(separators)

def order_of_elements(file_name, separators=None):
    return len(get_info(file_name, separators))