from textHandler import *

reader = FileReader("cats_dogs_and_trees.txt")

text = reader.get_entire_file_as_array()

writer = FileWriter("cats_dogs_and_trees_clean.txt")

writer.write_line_to_file(convert_list_to_sentence(text))

