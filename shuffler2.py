import random
import sys
from textHandler import *
import goal_two_input


def helper(word, key, sense):
	if word==key:
		return sense
	else:
		return word


def senses_in_sentenses(sentence, keywords, senses_dict):
	extra_sentenses = [sentence]
	for key in keywords:
		#print(len(extra_sentenses))
		#print(key)
		for tmp_sentence in extra_sentenses:
			if key in tmp_sentence:
				senses = senses_dict[key]
				for sense in senses:		
					new_sentence = [helper(w,key,sense) for w in tmp_sentence]
					extra_sentenses.append(new_sentence)
	return extra_sentenses



file_name = "test_text"
#file_name = "cats_dogs_and_trees"
#file_name = sys.argv[1]

nbr_of_repetitions = 1
#nbr_of_repetitions = int(sys.argv[2])



#Shuffle sentences in text
file_to_read = open("texts/" + file_name + ".txt", "r")
sentences = []

current_sentence = file_to_read.readline()
while(not (current_sentence == "")):
	sentences.append(current_sentence)
	current_sentence = file_to_read.readline()

file_to_read.close()


file_to_write = open("texts/" + file_name + "_shuffled.txt", "w+")


#for i in range(nbr_of_repetitions):
#	random.shuffle(sentences)

#	for j in range(len(sentences)):
#		file_to_write.write(sentences[j])

keywords,sensations = goal_two_input.get_input()

new_sentences = []
for sentence in sentences:
	new_sentences = new_sentences + (senses_in_sentenses(convert_sentence_to_list(sentence),keywords,sensations))
	#print("Hellu")

sentences = [convert_list_to_sentence(s)+" " for s in new_sentences]



repeated_sentences = []
for i in range(nbr_of_repetitions):
	repeated_sentences = repeated_sentences + sentences
random.shuffle(repeated_sentences)

for j in range(len(repeated_sentences)):
	file_to_write.write(repeated_sentences[j])

file_to_write.close()




#Clean text from unnecessary stuff
reader = FileReader("texts/" + file_name + "_shuffled.txt")

text = reader.get_entire_file_as_array()

reader.close_file()

writer = FileWriter("texts/" + file_name + "_shuffled_clean.txt")

writer.write_line_to_file(convert_list_to_sentence(text))

writer.close_file()

