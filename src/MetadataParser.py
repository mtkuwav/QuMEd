import os
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from typing import Optional
import re

class MetadataParser:
    def __init__(self, elements_dict):
        self.elements = elements_dict