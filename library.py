import os
from mutagen.easyid3 import EasyID3 as id3
from mutagen.flac import FLAC as flac
from typing import Optional




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
    extention = ""
    while (file_name[-1] != "."):
        extention = file_name[-1] + extention
        file_name = file_name[:-1]
    return extention





# ======================== FILE fFORMAT FUNCTIONS ========================


def get_name_structure(file_name: str):
    return












"""
edit the metadata of a .flac file.
"""
# i'll might add more parameters later, depending on what the user wants to edit and most importantly, my needs and what mutagen supports.
def edit_mp3_metadata(file_path: str, title: Optional[str] = None, artist: Optional[str] = None, album: Optional[str] = None, bpm: Optional[str] = None, genre: Optional[str] = None, release_date: Optional[str] = None, track_number: Optional[str] = None, disc_number: Optional[str] = None):
    audio = flac(file_path)
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