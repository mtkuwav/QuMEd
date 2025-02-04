import os
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from typing import Optional
import re



# ========================GLOBAL VARIABLES========================

# Elements specified by the user to get all the categories of the metadata.
ELEMENTS_OF_NAME = {"%A%": "artist",
                    "%a%": "album",
                    "%t%": "title",
                    "%n%": "track_number",
                    "%d%": "disc_number",
                    "%b%": "bpm",
                    "%g%": "genre",
                    "%r%": "release_date"}

TAGS_AVAILIBLE = [  "artist", 
                    "album", 
                    "title", 
                    "track_number", 
                    "disc_number", 
                    "bpm", 
                    "genre", 
                    "release_date"]



# ======================== FILE NAME GETTING FUNCTIONS ========================


def get_file_name (file_path: str) -> str:
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



def get_files_name(directory_path: str) -> tuple:
    """Return the name of the all the files from the file path in a string.

    Args:
        directory_path (str): path of the directory.

    Returns:
        tuple: An tuple of strings, each string being the name of a file in the 
        directory. If an error occurs, an empty tuple is returned.
    """    
    try:
        return tuple([f for f in os.listdir(directory_path) 
                if os.path.isfile(os.path.join(directory_path, f))])
    except Exception as e:
        print(f"Uh-Oh ! An error occurred: {e}")
        return ()



def get_file_extension (file_name: str) -> str:
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

def get_file_name_without_extension(file_name: str) -> str:
    """Gets the file name without its extension

    Args:
        file_name (str): the name of the file

    Returns:
        str: the name of the file without its extension
    """
    return file_name.split("." + get_file_extension(file_name))[0]





# ======================== FILE FORMAT FUNCTIONS ========================


# if the structure is "%n%. %a% - %t% - %A%" and the name is "01. Pattern Factory Operators - Red Card Stratagem (feat. Jankennpopp) - Custom Air Modulations.wav",
# it must return a dict with this structure : {"track_number" : 1 ,
#                                              "artist" : "Pattern Factory Operators" ,
#                                              "title" : "Red Card Stratagem (feat. Jankennpopp)" ,
#                                              "album" : "Custom Air Modulations"}


# def get_tags_by_structure(structure: str, file_name: str) -> dict:
#     tags = {}
#     pattern = structure
#
#     tags = {}
#     pattern = structure
#
#     # Replace placeholders with regex patterns
#     for key, value in ELEMENTS_OF_NAME.items():
#         pattern = pattern.replace(key, f"(?P<{value}>[^-]+)") #?P<{value}>.+?
#
#     # Compile the regex pattern
#     regex = re.compile(pattern)
#     match = regex.match(file_name)
#
#     if match:
#         tags = match.groupdict()
#
#         # Convert track number to integer
#         if 'track_number' in tags:
#             tags['track_number'] = int(tags['track_number'].split(".")[0])
#
#     return tags

# def get_tags_by_structure(separators: list, order_of_tags: list, file_name: str) -> dict:
#     index_oot = 0
#     index_separators = 0
#     tags = {}
#     for tag in order_of_tags:
#         #print(f"tag :{type(tag)}, {tag}")


#         buffer=file_name.split(separators[index_separators])
#         #print(f"buffer : {buffer}")
#         tags[order_of_tags[index_oot]] = buffer[0]
#         index_oot += 1

#     return tags





def get_tags_by_structure(structure: str, file_name: str) -> dict:
    """Associates in a dict every tag of the file name with its correct key,
    based on the scheme given by the user.

    Args:
        structure (str): how the file name is organized
        file_name (str): the name of the file

    Returns:
        dict: a dict containing the tags presents in the file name
    """
    tags = {}
    separators = get_separators(structure)
    file_name_index = 0
    tag_index = 0
    
    #print(tags_keys)
    
    for i in range(len(structure) - 2):
        if (structure[i] == "%" and structure[i+2] == "%"):
            tags[ELEMENTS_OF_NAME["%" + structure[i+1] + "%"]] = ""
    
    tags_keys_list = list(tags.keys())
    
    while file_name_index < len(file_name):
        match = False
        for separator in separators: #marche pas psq ça parcourt tout 
            if file_name[file_name_index:file_name_index+len(separator)] == separator:
                match = True
                file_name_index += len(separator)
                tag_index += 1
                separators = separators[1:]
                break
    
        if not match:
            tags[tags_keys_list[tag_index]] += file_name[file_name_index]
            file_name_index += 1
    return tags


def make_integer_tags(tags: dict) -> None:
    if tags["bpm"]:
        print("oui")
        

def check_if_discnb_and_tracknb_sticked(structure: str, file_name: str) -> None:
    


def get_separators(structure: str) -> list:
    """Gets every separator of the structure (every string that is not in
    ELEMENTS_OF_NAME.keys()), and so of the file name.

    Args:
        structure (str): structure of the file name

    Returns:
        tuple: a tuple which contains every separators of the structure and so 
        of the file name.
    """
    pattern = re.compile(r'%[a-zA-Z]%')
    
    matches = pattern.finditer(structure)
    
    separators = []
    last_end = 0
    
    for match in matches:
        start, end = match.span()
        if start > last_end:
            separators.append(structure[last_end:start])
        last_end = end
    
    if last_end < len(structure):
        separators.append(structure[last_end:])
    
    return separators




# I'll might add more parameters later, depending on what the user wants to edit and most importantly, my needs and what mutagen supports.
def edit_mp3_metadata(  file_path: str, 
                        title: Optional[str] = None, 
                        artist: Optional[str] = None, 
                        album: Optional[str] = None, 
                        bpm: Optional[str] = None, 
                        genre: Optional[str] = None, 
                        release_date: Optional[str] = None, 
                        track_number: Optional[str] = None, 
                        disc_number: Optional[str] = None   ) -> None:
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




# def get_separators(structure: str) -> tuple:
#     separators_list = []
#     separator = ""
#     for i in range(len(structure) - 2):
#         j = i + 1
#         if structure[i] == "%":
#             while structure[j] != "%":
#                 separator += structure[j]
#                 j += 1
#             separators_list.append(separator)
#         separator = ""
#     return tuple(separators_list)

# def get_separators(structure: str) -> tuple:
#     """Gets every separator of the structure (every string that is not in
#     ELEMENTS_OF_NAME.keys()), and so of the file name.

#     Args:
#         structure (str): structure of the file name

#     Returns:
#         tuple: a tuple which contains every separators of the structure and so 
#         of the file name.
#     """
#     separators = []
#     i = 0
    
#     while i < len(structure):
        
#         if structure[i] == "%" and i + 2 < len(structure) and structure[i+2] == "%":
#             i += 3
        
#         else:
#             separator = ""
#             while i < len(structure) and (structure[i] != "%" or 
#                         (i + 2 < len(structure) and structure[i+2] != "%")):
                
#                 separator += structure[i]
#                 i += 1
                
#             if separator:
#                 separators.append(separator)
#     return tuple(separators)