from textHandler import *
from math import *
import bisect
from scipy import spatial

def safe_div(x,y):
	if y == 0:
		return 0
	return x/(y*1.0)

class WordVectorModel:
	def __init__(self, text_handler, context_size):
		self.text_handler = text_handler
		self.context_size = context_size #number of words on each side of target word (before and after it) that are in included in context

		self.text = text_handler.get_entire_file_as_array()
		print("text len: " + str(len(self.text)))
		self.words = []
		#print("dummy")
		for w in self.text:
			if not w in self.words:
				self.words.append(w)

		self.matrix = [ [0.0] * len(self.words) for _ in range(len(self.words)) ]
		self.word_occurences = [0] * len(self.words)
	#End __init__()

	def update_matrix(self):
		#print("yo!")
		#print(self.words)
		for time in range(len(self.text)):
			target_word = self.text[time]
			target_word_index = self.words.index(target_word)
			for i in range(1, self.context_size+1):
				if time - i >= 0:
					#print(target_word)
					context_word = self.text[time-i]
					context_word_index = self.words.index(context_word)
					self.matrix[target_word_index][context_word_index] = self.matrix[target_word_index][context_word_index] + 1
				if time + i < len(self.text):
					#print(target_word)
					context_word = self.text[time+i]
					context_word_index = self.words.index(context_word)
					self.matrix[target_word_index][context_word_index] = self.matrix[target_word_index][context_word_index] + 1

			self.word_occurences[target_word_index] = self.word_occurences[target_word_index] + 1

		for i in range(len(self.words)):
			self.matrix[i] = [safe_div(x,y) for x, y in zip(self.matrix[i], self.word_occurences)]
	#End update_matrix()

	def get_ordered_associations(self,target_word):
		target_word_index = self.words.index(target_word)
		result_list_values = []
		result_list_words = []
		for i in range(len(self.words)):
			if not i == target_word_index:
				#print(self.matrix[target_word_index])
				#print(self.matrix[i])
				r = spatial.distance.cosine(self.matrix[target_word_index],self.matrix[i])
				insertion_point = bisect.bisect(result_list_values, r)

				result_list_values.insert(insertion_point, r)
				result_list_words.insert(insertion_point, self.words[i])
		return result_list_words[0:20],result_list_values[0:20]
	#End get_ordered_associations

#text_handler = FileReader("testtext.txt")
#text_handler = FileReader("UK_weather_2018_march_clean.txt")
#text_handler = FileReader("fables_and_animal_stories_all_clean.txt")
text_handler = FileReader("texts/test_text_shuffled_clean.txt")
wvm = WordVectorModel(text_handler, 2)
wvm.update_matrix()
#print("Associations for 'dogs'")
#print(wvm.get_ordered_associations("dogs"))
#print("Associations for 'cats'")
#print(wvm.get_ordered_associations("cats"))
#print("Associations for 'puppies'")
#print(wvm.get_ordered_associations("puppies"))

print("Nbr of unique words in text file: " + str(len(wvm.words)))
print(wvm.words)
print()
print("Associations for 'dog'")
words,dist = wvm.get_ordered_associations("dog")
#print(dist[0])
for i in range(20):
	print(" %s : %f " % (words[i],dist[i]))




