import os
from mutagen.easyid3 import EasyID3 as id3
from mutagen.flac import FLAC as flac

"""
Return the title of the file from the file path.
"""
def get_file_title (file_path):
    return os.path.basename(file_path)

"""
Return the extension of the file from the file path.
"""
def get_file_extension (file_path):
    return os.path.splitext(file_path)[1]


"""
edit the metadata of a .flac file.
"""
# i'll might add more parameters later, depending on what the user wants to edit and most importantly, my needs and what mutagen supports.
def edit_mp3_metadata(file_path, title=None, artist=None, album=None, bpm=None, genre=None, release_date=None, track_number=None, disc_number=None):
    audio = flac(file_path)
    audio['title'] = title
    audio['artist'] = artist
    audio['album'] = album
    audio.save()