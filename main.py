import library

#print(library.get_files_name("C:/Users/ourea/Music/Pattern Factory Operators/Custom Air Modulations"))
test_name = "01. Pattern Factory Operators - Red Card Stratagem (feat. Jankennpopp) - Custom Air Modulations.wav"
# print(library.get_file_extension("01. Pattern Factory Operators - Red Card Stratagem (feat. Jankennpopp) - Custom Air Modulations.wav"))
structure = "%n%. %a% - %t% - %A%"
file_name = "01. Pattern Factory Operators - Red Card Stratagem (feat. Jankennpopp) - Custom Air Modulations.wav"
print(library.get_tags_by_structure(structure, file_name))