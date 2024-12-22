import library

#print(library.get_files_name("C:/Users/ourea/Music/Pattern Factory Operators/Custom Air Modulations"))
test_name = "01. Pattern Factory Operators - Red Card Stratagem (feat. Jankennpopp) - Custom Air Modulations.wav"
# print(library.get_file_extension("01. Pattern Factory Operators - Red Card Stratagem (feat. Jankennpopp) - Custom Air Modulations.wav"))
structure = "%n%. %a% - %t% - %A%"
structure2 = "%n% - %t%, %A%, (%r%)"
# separator = " - "
# song = 2
# file_name = "01. Pattern Factory Operators - Red Card Stratagem (feat. Jankennpopp) - Custom Air Modulations.wav"
# print(library.get_tags_by_structure(structure, file_name))


separators=[". ", " - "]
order_of_tags = ["track_number", "artist", "title", "album"]
print(library.get_tags_by_structure(structure, test_name))

# print(library.get_number_of_separators(separators, test_name))

# print(library.get_file_extension(test_name))
# print(library.get_file_name_without_extension(test_name))

# print(library.get_separators(structure))
# print(library.get_separators(structure2))