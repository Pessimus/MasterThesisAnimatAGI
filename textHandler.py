#For reading a text

#A class for reprecenting and handling the reading of a text file.
class FileReader:
	def __init__(self, file_name):
		self.file_name = file_name
		self.file_object = open(file_name, "r")
		self.current_sentence = []
		self.end_of_file = False
	#End __init__()

	#Gives the next sentence in the file.
	def get_next_sentence(self):
		return self.file_object.readline()
	#End get_next_sentence()

	#Returns the next word in the file, and updates the variable current_sentence.
	def get_next_word(self): 
		if len(self.current_sentence) == 0:
			self.current_sentence = convert_sentence_to_list(remove_sign_from_string(self.get_next_sentence()).lower())
			if len(self.current_sentence) == 0:
				self.end_of_file = True
				return ""
		return self.current_sentence.pop(0)
	#End get_next_word()

	#returns a array of all the words in the remaining fiel
	def get_entire_file_as_array(self):
		result = []
		while not self.end_of_file:
			result.append(self.get_next_word())
		result.pop() #remove the dummy value that is returned at when all words are found.
		return result
	#End get_entire_file_as_array()

	#Closes the current file so that it can no longer be used.
	def close_file(self):
		self.file_object.close()
	#End close_file()
#End class fileReader

#A class for reprecenting and handling the writing to a text file.
class FileWriter:
	def __init__(self, file_name):
		self.file_name = file_name
		self.file_object = open(file_name, "w+")
	#End __init__()

	#Writes the specified input to the file as a new line.
	def write_line_to_file(self, sentence):
		self.file_object.write(sentence+"\n")
	#End write_line_to_file()

	#Writes a list of lines to the file.
	def write_lines_to_file(self, lines):
		for line in lines:
			self.write_line_to_file(line)
	#End write_lines_to_file()

	#Closes the current file so that it can no longer be used.
	def close_file(self):
		self.file_object.close()
	#End close_file()

#End class fileReader

#Given a sentence, splits it on white spaces to make a list of the words.
def convert_sentence_to_list(sentence):
	return sentence.split()
#End convert_sentence_to_list()

#Given a list of words, concatenates them into a sentence with spaces in between each word.
def convert_list_to_sentence(list):
	return " ".join(list)
#End convert_list_to_sentence()

#Given a word, splits it into a list of chars.
def convert_word_to_list(word):
	res_list = []
	for char in word:
		res_list.append(char)
	return res_list
#End convert_word_to_list()

#Given a list of chars, concatenates them into a word.
def convert_list_to_word(list):
	return "".join(list)
#End convert_list_to_word()

#Remove special signs from a string.
def remove_sign_from_string(string):
	res_list = []

	for char in string:
		if not char in "'\"`´“’‘.,?!-;:/\n":
			res_list.append(char)
	return "".join(res_list)
#End remove_sign_from_string()

