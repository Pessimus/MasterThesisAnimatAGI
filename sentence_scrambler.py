import random
import sys

nbr_of_repetitions = 3

#file_name = "test_text"
file_name = "cats_dogs_and_trees"
file_name = sys.argv[1]

file_to_read = open(file_name + ".txt", "r")

sentences = []

current_sentence = file_to_read.readline()
while(not (current_sentence == "")):
	#print("current: " + current_sentence)
	sentences.append(current_sentence)
	current_sentence = file_to_read.readline()
#print("end of file")

file_to_read.close()

#print("sentences:" + str(sentences))

file_to_write = open(file_name + "_shuffled.txt", "w+")

for i in range(nbr_of_repetitions):
	random.shuffle(sentences)

	for j in range(len(sentences)):
		file_to_write.write(sentences[j])

