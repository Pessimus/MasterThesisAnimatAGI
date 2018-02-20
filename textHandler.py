#For reading a text

#A class for reprecenting and handling a text file.
class fileReader:
	def __init__(self, fileName):
		self.fileName = fileName
		self.fileObject = open(fileName, "r")
	#End __init__()

	#Gives the next sentence in the file.
	def getNextSentence(self):
		return self.fileObject.readline()
	#End getNextSentence()

	#Closes the current file so that it can no longer be used.
	def closeFile(self):
		self.fileObject.close()
	#End closeFile()
#End class fileReader

#Given a sentence, splits it on white spaces to make a list of the words.
def convertSentenceToList(sentence):
	return sentence.split()
#End convertSentenceToList()

#Given a list of words, concatenates them into a sentence with spaces in between each word.
def convertListToSentence(list):
	return " ".join(list)
#End convertListToSentence()

#Given a word, splits it into a list of chars.
def convertWordToList(word):
	res_list = []
	for char in word:
		res_list.append(char)
	return res_list
#End convertWordToList()

#Given a list of chars, concatenates them into a word.
def convertListToWord(list):
	return "".join(list)
#End convertListToWord()

#Remove special signs from a string.
def removeSignFromString(string):
	res_list = []

	for char in string:
		if not char in ".,?!-;:/\n":
			res_list.append(char)
	return "".join(res_list)
#End removeSignFromString()

