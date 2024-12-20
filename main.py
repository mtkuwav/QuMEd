import library

#print(library.get_files_name("C:/Users/ourea/Music/Pattern Factory Operators/Custom Air Modulations"))
test_name = "01. Pattern Factory Operators - Red Card Stratagem (feat. Jankennpopp) - Custom Air Modulations.wav"
# print(library.get_file_extension("01. Pattern Factory Operators - Red Card Stratagem (feat. Jankennpopp) - Custom Air Modulations.wav"))
# structure = "%n%. %a% - %t% - %A%"
# separator = " - "
# song = 2
# file_name = "01. Pattern Factory Operators - Red Card Stratagem (feat. Jankennpopp) - Custom Air Modulations.wav"
# print(library.get_tags_by_structure(structure, file_name))


separators=[". ", " - "]
order_of_tags = ["track_number", "artist", "title", "album"]
print(library.get_tags_by_structure(separators, order_of_tags, test_name))