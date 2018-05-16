from Chunking_Animat.node import *
from Chunking_Animat.nodes import *
from Chunking_Animat.environment import *
from Chunking_Animat.actionNodes import *
from Chunking_Animat.temporalActionNodes import *
from textHandler import *
from controller import *
from Chunking_Animat.network import *
from Chunking_Animat.animat import *
from random import shuffle
import random
import datetime
from WordVectorModel import *
import goal_two_input

def create_nodes_for_alphabet(test_environment):
	sensor_node_a = SensorNode(name = "a-sensor",sensor = "a", environment =  test_environment)
	sensor_node_b = SensorNode(name = "b-sensor",sensor = "b", environment =  test_environment)
	sensor_node_c = SensorNode(name = "c-sensor",sensor = "c", environment =  test_environment)
	sensor_node_d = SensorNode(name = "d-sensor",sensor = "d", environment =  test_environment)
	sensor_node_e = SensorNode(name = "e-sensor",sensor = "e", environment =  test_environment)
	sensor_node_f = SensorNode(name = "f-sensor",sensor = "f", environment =  test_environment)
	sensor_node_g = SensorNode(name = "g-sensor",sensor = "g", environment =  test_environment)
	sensor_node_h = SensorNode(name = "h-sensor",sensor = "h", environment =  test_environment)
	sensor_node_i = SensorNode(name = "i-sensor",sensor = "i", environment =  test_environment)
	sensor_node_j = SensorNode(name = "j-sensor",sensor = "j", environment =  test_environment)
	sensor_node_k = SensorNode(name = "k-sensor",sensor = "k", environment =  test_environment)
	sensor_node_l = SensorNode(name = "l-sensor",sensor = "l", environment =  test_environment)
	sensor_node_m = SensorNode(name = "m-sensor",sensor = "m", environment =  test_environment)
	sensor_node_n = SensorNode(name = "n-sensor",sensor = "n", environment =  test_environment)
	sensor_node_o = SensorNode(name = "o-sensor",sensor = "o", environment =  test_environment)
	sensor_node_p = SensorNode(name = "p-sensor",sensor = "p", environment =  test_environment)
	sensor_node_q = SensorNode(name = "q-sensor",sensor = "q", environment =  test_environment)
	sensor_node_r = SensorNode(name = "r-sensor",sensor = "r", environment =  test_environment)
	sensor_node_s = SensorNode(name = "s-sensor",sensor = "s", environment =  test_environment)
	sensor_node_t = SensorNode(name = "t-sensor",sensor = "t", environment =  test_environment)
	sensor_node_u = SensorNode(name = "u-sensor",sensor = "u", environment =  test_environment)
	sensor_node_v = SensorNode(name = "v-sensor",sensor = "v", environment =  test_environment)
	sensor_node_w = SensorNode(name = "w-sensor",sensor = "w", environment =  test_environment)
	sensor_node_x = SensorNode(name = "x-sensor",sensor = "x", environment =  test_environment)
	sensor_node_y = SensorNode(name = "y-sensor",sensor = "y", environment =  test_environment)
	sensor_node_z = SensorNode(name = "z-sensor",sensor = "z", environment =  test_environment)

	motor_node_a = MotorNode(name = "a-motor",motor = "a", environment =  test_environment)
	motor_node_b = MotorNode(name = "b-motor",motor = "b", environment =  test_environment)
	motor_node_c = MotorNode(name = "c-motor",motor = "c", environment =  test_environment)
	motor_node_d = MotorNode(name = "d-motor",motor = "d", environment =  test_environment)
	motor_node_e = MotorNode(name = "e-motor",motor = "e", environment =  test_environment)
	motor_node_f = MotorNode(name = "f-motor",motor = "f", environment =  test_environment)
	motor_node_g = MotorNode(name = "g-motor",motor = "g", environment =  test_environment)
	motor_node_h = MotorNode(name = "h-motor",motor = "h", environment =  test_environment)
	motor_node_i = MotorNode(name = "i-motor",motor = "i", environment =  test_environment)
	motor_node_j = MotorNode(name = "j-motor",motor = "j", environment =  test_environment)
	motor_node_k = MotorNode(name = "k-motor",motor = "k", environment =  test_environment)
	motor_node_l = MotorNode(name = "l-motor",motor = "l", environment =  test_environment)
	motor_node_m = MotorNode(name = "m-motor",motor = "m", environment =  test_environment)
	motor_node_n = MotorNode(name = "n-motor",motor = "n", environment =  test_environment)
	motor_node_o = MotorNode(name = "o-motor",motor = "o", environment =  test_environment)
	motor_node_p = MotorNode(name = "p-motor",motor = "p", environment =  test_environment)
	motor_node_q = MotorNode(name = "q-motor",motor = "q", environment =  test_environment)
	motor_node_r = MotorNode(name = "r-motor",motor = "r", environment =  test_environment)
	motor_node_s = MotorNode(name = "s-motor",motor = "s", environment =  test_environment)
	motor_node_t = MotorNode(name = "t-motor",motor = "t", environment =  test_environment)
	motor_node_u = MotorNode(name = "u-motor",motor = "u", environment =  test_environment)
	motor_node_v = MotorNode(name = "v-motor",motor = "v", environment =  test_environment)
	motor_node_w = MotorNode(name = "w-motor",motor = "w", environment =  test_environment)
	motor_node_x = MotorNode(name = "x-motor",motor = "x", environment =  test_environment)
	motor_node_y = MotorNode(name = "y-motor",motor = "y", environment =  test_environment)
	motor_node_z = MotorNode(name = "z-motor",motor = "z", environment =  test_environment)

	sensors = [sensor_node_a, sensor_node_b, sensor_node_c, sensor_node_d, sensor_node_e, sensor_node_f, sensor_node_g, sensor_node_h, sensor_node_i, sensor_node_j, sensor_node_k, sensor_node_l, sensor_node_m, sensor_node_n, sensor_node_o, sensor_node_p, sensor_node_q, sensor_node_r, sensor_node_s, sensor_node_t, sensor_node_u, sensor_node_v, sensor_node_w, sensor_node_x, sensor_node_y, sensor_node_z]
	motors = [motor_node_a, motor_node_b, motor_node_c, motor_node_d, motor_node_e, motor_node_f, motor_node_g, motor_node_h, motor_node_i, motor_node_j, motor_node_k, motor_node_l, motor_node_m, motor_node_n, motor_node_o, motor_node_p, motor_node_q, motor_node_r, motor_node_s, motor_node_t, motor_node_u, motor_node_v, motor_node_w, motor_node_x, motor_node_y, motor_node_z]

	#sensors = [sensor_node_d,sensor_node_o,sensor_node_g]
	#motors = [motor_node_d,motor_node_o,motor_node_g]

	#from random import shuffle
	#shuffle(sensors)
	#shuffle(motors)

	return sensors, motors

def evalaute_chunking():
	verbose = True
	TIME_OF_START_OF_RUN = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
	TIME_OF_START_OF_BABBLING = ""
	TIME_OF_START_OF_LEARNING_WORDS = ""
	TIME_OF_START_OF_LEARNING_ASSOCIATIONS = ""
	TIME_OF_START_OF_EVALUATION = ""
	TIME_OF_END = ""

	AVERAGE_NUMBER_OF_OCCURRENCES_OF_EACH_WORD = 15
	SEQ_FORMATION_PROBABILITY = 1
	MEMORY_CAPACITY = 7
	SEQ_FORMATION_MAX_ATTEMPTS = 10

	#INPUT_FILE_NAME = "texts/cats_dogs_and_trees_shuffled_clean.txt"
	INPUT_FILE_NAME = "texts/test_text.txt"
	#INPUT_FILE_NAME = "texts/one_sentence.txt"
	#INPUT_FILE_NAME = "texts/small.txt"
	#INPUT_FILE_NAME = "texts/test_text_shuffled_clean.txt"
	input_file = FileReader(INPUT_FILE_NAME)
	entire_text = input_file.get_entire_file_as_array()
	unique_words = []
	for word in entire_text:
		if not word in unique_words:
			unique_words.append(word)

	TOTAL_NUMBER_OF_WORDS = len(unique_words)

	MAX_TIME = AVERAGE_NUMBER_OF_OCCURRENCES_OF_EACH_WORD * TOTAL_NUMBER_OF_WORDS + AVERAGE_NUMBER_OF_OCCURRENCES_OF_EACH_WORD * TOTAL_NUMBER_OF_WORDS * 5 #*2 to allow for spaces between words.

	test_environment = Environment()	
	sensors, motors = create_nodes_for_alphabet(test_environment)
	totlal_number_of_sensors = len(sensors)
	test_animat = Animat("TheOnkeydogdonk", sensors, motors, memory_capacity = MEMORY_CAPACITY, seq_formation_probability = SEQ_FORMATION_PROBABILITY, seq_formation_max_attempts = SEQ_FORMATION_MAX_ATTEMPTS)

	time = 0

	#//-----------------------------------------------------------------------------------------------------------------------------------------------------\\
	TIME_OF_START_OF_BABBLING = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
#	if verbose:
#		print("Starting babbling")
#	#Let the animat discover generators for the sensors by babbling
#	while((-1) in test_animat.network.generator_list):
#	#for y in range(0,300):
#		time = time + 1
#		test_animat.update(time, babble = True)
#		test_environment.update()
#
	RESULT_time_to_learn_all_generators = time
#
#	print(test_animat.network.sequence_matrix)
#
#	#Handle transition from babbling
#	time = time + 1
#	test_animat.update(time, babble = False)
#	test_environment.update()
#
#
#	if verbose:
#		print("Done babbling")
#		animat_nodes_as_strings = [n.get_word() for n in (test_animat.network.sensors + test_animat.network.perception_nodes)]
#		print(animat_nodes_as_strings)

	#\\-----------------------------------------------------------------------------------------------------------------------------------------------------//
	
	#//-----------------------------------------------------------------------------------------------------------------------------------------------------\\
	#Let the animat learn new words
	SPACE = True

	TIME_OF_START_OF_LEARNING_WORDS = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
	if verbose:
		print("Starting learning words")
	#Train the Animat
	while time < MAX_TIME + RESULT_time_to_learn_all_generators:
		time = time + 1
		#update environment
		index = np.random.randint(0, TOTAL_NUMBER_OF_WORDS)
		word = unique_words[index]

		for char in word:
			test_environment.next_state = char
			test_environment.update()

			#Update the Animat
			test_animat.update(time)

			time = time + 1

		if(SPACE):
			#Give the Animat a space between words
			time = time + 1
			test_environment.next_state = " "
			test_environment.update()
			test_animat.update(time)
		#print(time)
	#End for loop
	if verbose:
		print("Done learning words")

		#for i in range(0,len(test_animat.network.sequence_matrix)):
		#	print([len(e) for e in test_animat.network.sequence_matrix[i]])

		animat_nodes_as_strings = [n.get_word() for n in (test_animat.network.sensors + test_animat.network.perception_nodes)]
		print(animat_nodes_as_strings)

		for word in unique_words:
			if(word in animat_nodes_as_strings):
				print("Animat has learnt the word: "+word)
			else:
				print("Animat has not learnt word: "+word)

		#print("Nbr of nodes = " + str(test_animat.network.total_number_of_input_nodes))
		#print("Association matrix sum = " + str(sum([sum(s) for s in test_animat.network.time_extended_conditional_matrix])))
	#\\-----------------------------------------------------------------------------------------------------------------------------------------------------//
	
	# #//-----------------------------------------------------------------------------------------------------------------------------------------------------\\
	# #Let the Animat lear to associate
	# TIME_OF_START_OF_LEARNING_ASSOCIATIONS = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
	# if verbose:
	# 	print("Starting learning associations")
	# test_animat.seq_formation_probability = 0
	# test_animat.learn_to_associate = True

	# #last_word = "!"

	# for word in entire_text:
	# 	time = time + 1
	# 	#test_environment.temporal_state = word
	# 	test_environment.next_temporal_state = word
	# 	test_environment.update()

	# 	test_animat.update_goal_one_version(time,len(word))

	# 	#Give the Animat a space between words
	# 	time = time + 1
	# 	#test_environment.temporal_state = " "
	# 	test_environment.next_temporal_state = " "
	# 	test_environment.update()
	# 	test_animat.update_goal_one_version(time,1)

	# 	#tas = [n.get_word() for n in test_animat.network.get_topactive_nodes()]
	# 	#if("la" in tas):
	# 	#	print("Ehuru evad?!")
	# 	#	print(last_word)
	# 	#	print(word)

	# 	#last_word = word

	# if verbose:
	# 	print("Done learning associations")
	# 	#print("Nbr of nodes = " + str(test_animat.network.total_number_of_input_nodes))
	# #\\-----------------------------------------------------------------------------------------------------------------------------------------------------//
	
	# #//-----------------------------------------------------------------------------------------------------------------------------------------------------\\
	# #Evaluate
	# TIME_OF_START_OF_EVALUATION = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
	# if verbose:
	# 	print("Begining actual evaluation")
	# test_animat.learn_to_associate = False

	# file = FileWriter("evaluationIO/" + "Goal1_Result_from" + TIME_OF_START_OF_RUN + "_to" + datetime.datetime.now().strftime("%y%m%d_%H%M%S") + ".m")
	# file.write_line_to_file("")

	# file.write_line_to_file("% Animat Associations:")

	# animat_associations = []

	# for word in unique_words:
	# 	time = time + 1
	# 	#test_environment.temporal_state = word
	# 	test_environment.next_temporal_state = word
	# 	test_environment.update()

	# 	test_animat.update_goal_one_version(time,len(word))

	# 	word_associations = test_animat.associate()
	# 	animat_associations.append(word_associations)
	# 	file.write_line_to_file("animat_associations_"+word+" = " + str(word_associations) + ";")

	# 	#Give the Animat a space between words
	# 	time = time + 1
	# 	#test_environment.temporal_state = " "
	# 	test_environment.next_temporal_state = " "
	# 	test_environment.update()
	# 	test_animat.update_goal_one_version(time,1)

	# #End getting associations from the Animat

	# file.write_line_to_file("")
	# file.write_line_to_file("%Vector Space Associations:")
	# file.write_line_to_file("")


	# reader = FileReader(INPUT_FILE_NAME)
	# wvm = WordVectorModel(reader, MEMORY_CAPACITY-1)
	# wvm.update_matrix()

	# vector_space_associations = []
	# for word in unique_words:
	# 	#print("LOOOOOP")
	# 	word_associations, association_values = wvm.get_ordered_associations(word)
	# 	vector_space_associations.append(word_associations)
	# 	#print(len(word_associations))
	# 	file.write_line_to_file("vsm_associations_"+word+" = " + str(word_associations) + ";")
	# #End getting associations from the vector space

	# score = 0
	# for i in range (0,len(unique_words)):
	# 	x = animat_associations[i]
	# 	y = vector_space_associations[i]
	# 	for word in y:
	# 		if word in x:
	# 			score = score + 1

	# max_score = len(unique_words)*10

	# result = (score*1.0)/max_score

	# print(result)
	# file.write_line_to_file("")
	# file.write_line_to_file("%Result is: "+str(score)+" of "+str(max_score))
	# file.write_line_to_file("result = "+str(result))


	# TIME_OF_END = datetime.datetime.now().strftime("%y%m%d_%H%M%S")

	# file.write_line_to_file("")
	# file.write_line_to_file("TIME_OF_START_OF_RUN = " + TIME_OF_START_OF_RUN)
	# file.write_line_to_file("TIME_OF_START_OF_BABBLING = " + TIME_OF_START_OF_BABBLING)
	# file.write_line_to_file("TIME_OF_START_OF_LEARNING_WORDS = " + TIME_OF_START_OF_LEARNING_WORDS)
	# file.write_line_to_file("TIME_OF_START_OF_LEARNING_ASSOCIATIONS = " + TIME_OF_START_OF_LEARNING_ASSOCIATIONS)
	# file.write_line_to_file("TIME_OF_START_OF_EVALUATION = " + TIME_OF_START_OF_EVALUATION)
	# file.write_line_to_file("TIME_OF_END = " + TIME_OF_END)

	# tmp_animat_words = [n.get_word() for n in (test_animat.network.sensors + test_animat.network.perception_nodes)]
	# not_learnt_words = []
	# nbr_words_learnt = 0
	# for w in unique_words:
	# 	if w in tmp_animat_words:
	# 		nbr_words_learnt = nbr_words_learnt + 1
	# 	else:
	# 		not_learnt_words.append(w)

	# file.write_line_to_file("")
	# file.write_line_to_file("nbr_words_learnt = " + str(nbr_words_learnt) + ";")
	# file.write_line_to_file("not_learnt_words = " + str(not_learnt_words) + ";")	
	# #End evaluate_goal_one()




evalaute_chunking()
