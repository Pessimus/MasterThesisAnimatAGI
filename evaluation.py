from node import *
from nodes import *
from temporalNodes import *
from environment import *
from actionNodes import *
from temporalActionNodes import *
from textHandler import *
from controller import *
from network import *
from animat import *
from random import shuffle
import random
import datetime

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

	from random import shuffle
	shuffle(sensors)
	shuffle(motors)

	return sensors, motors

def evaluate_step_one():
	#test_how_often_the_animat_learns_the_entire_alphabet():	
	print("------------------Testing how often the animat learns the entire alphabet------------------")
	import numpy as np
	avg_nbr = 100
	tests_to_run = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300]

	print("Running tests with the nomber of iterations to babble set to:")
	print(tests_to_run)
	print("And averages over %d averaging runs." % (avg_nbr))

	results_all_generators_found = []
	results_avg_number_of_generators_found = []

	for nbr_iterations in tests_to_run:
		#start a test
		stats = np.zeros(avg_nbr)
		for test_number in range(1,avg_nbr+1): #run test several (avg_nbr) times to average.
			test_environment = Environment()
		
			sensors, motors = create_nodes_for_alphabet(test_environment)
		
			totlal_number_of_sensors = len(sensors)

			from random import shuffle
			shuffle(sensors)
			shuffle(motors)

			test_animat = Animat("TheDoggo", sensors, motors)
			#number_of_babble_iterations = nbr_iterations

			#let the animat learn
			for x in range(1, nbr_iterations+1): #+1 needed ass the loop does NOT include the last iteration
				test_animat.update(x)
				test_environment.update()

			generators = test_animat.network.generator_list

			number_of_correct_generators = 0
			for node in sensors:
				index = node.get_index()
				generator_index = generators[index]
				if not generator_index == -1: #does have a generator.
					if node.getWord() == motors[generator_index].getWord(): #is the right sensor.
						number_of_correct_generators = number_of_correct_generators + 1

			stats[test_number-1] = number_of_correct_generators
			#print("Number of correct generators is %d of %d, when babbling for %d iterations." % (number_of_correct_generators, totlal_number_of_sensors, nbr_iterations))
		#print(stats)
		result = sum([value == totlal_number_of_sensors for value in stats])
		#print(result)
		
		avg_number_of_generators_found = sum(stats)/avg_nbr

		results_all_generators_found.append(result/avg_nbr)
		#results_avg_number_of_generators_found.append(avg_number_of_generators_found/totlal_number_of_sensors)
		results_avg_number_of_generators_found.append(float(format(avg_number_of_generators_found/totlal_number_of_sensors, '.2f')))
	
	print("Percentage of times that all generators were found for the different tests:")
	print(results_all_generators_found)
	print("Average percentage of generators found for the different tests:")
	print(results_avg_number_of_generators_found)

	file = FileWriter("output/babbling_result.m")
	file.writeLineToFile("clear all, clf, clc")
	file.writeLineToFile("%The tests to run")
	file.writeLineToFile("tests_to_run = "+str(tests_to_run))
	file.writeLineToFile("%Percentage of times that all generators were found for the different tests:")
	file.writeLineToFile("results_all_generators_found = "+str(results_all_generators_found))
	file.writeLineToFile("% Average percentage of generators found for the different tests:")
	file.writeLineToFile("results_avg_number_of_generators_found = "+str(results_avg_number_of_generators_found))
	file.writeLineToFile("plot(tests_to_run,results_all_generators_found)")
	file.writeLineToFile("figure")
	file.writeLineToFile("yyaxis left")
	file.writeLineToFile("ylabel('Percentage of runs where all generators were found')")
	file.writeLineToFile("plot(tests_to_run,results_all_generators_found)")
	file.writeLineToFile("hold on")
	file.writeLineToFile("yyaxis right")
	file.writeLineToFile("ylabel('Average number of generators found');")
	file.writeLineToFile("plot(tests_to_run,results_avg_number_of_generators_found)")
	file.writeLineToFile("title('Statistics of how well the Animat finds generators');")
	file.writeLineToFile("xlabel('Number of timesteps spent babbling');")
	#file.writeLineToFile("legend('Runs where all generators were found','Average number of generators found','Location','east')")

def evaluate_step_two():
	#Define constatns (for this run)
	TOTAL_NUMBER_OF_WORDS = 10
	AVERAGE_NUMBER_OF_OCCURENCES_OF_EACH_WORD = 100
	SEQ_FORMATION_PROBABILITY = 1/float(25)

	#Define constatns (for all runs)
	TEMPORAL_MEMORY_CAPACITY = 5
	SEQ_FORMATION_MAX_ATTEMPTS = 10
	MAX_TIME = AVERAGE_NUMBER_OF_OCCURENCES_OF_EACH_WORD * TOTAL_NUMBER_OF_WORDS *2 #*2 to allow for spaces between words.
	INPUT_FILE_NAME = "evaluationIO/animal_words.txt"

	#Create the Animat
	test_environment = Environment()	
	sensors, motors = create_nodes_for_alphabet(test_environment)

	totlal_number_of_sensors = len(sensors)
	test_animat = Animat("TheCat", sensors, motors, temporal_memory_capacity = TEMPORAL_MEMORY_CAPACITY, seq_formation_probability = SEQ_FORMATION_PROBABILITY, seq_formation_max_attempts = SEQ_FORMATION_MAX_ATTEMPTS)

	#Create arrays for words to input to the animate
	input_file = FileReader(INPUT_FILE_NAME)
	all_words = input_file.get_entire_file_as_array()
	words_to_use = all_words[0:TOTAL_NUMBER_OF_WORDS]

	#Arrays to store results.
	RESULT_number_of_words_learnt = []
	RESULT_number_of_perception_nodes = []
	RESULT_word_occurenses = [0] * TOTAL_NUMBER_OF_WORDS

	#Train the Animat
	t = 0
	while t < MAX_TIME:
		t = t + 1
		#update environment
		index = np.random.randint(0, TOTAL_NUMBER_OF_WORDS)
		word = words_to_use[index]
		test_environment.temporalState = word

		#Update the Animat
		test_animat.update(t,len(word))

		#update results
		tmp_animat_words = [n.getWord() for n in test_animat.network.perception_nodes]
		c = 0
		for w in words_to_use:
			if w in tmp_animat_words:
				c = c + 1
		RESULT_number_of_words_learnt.append(c)
		RESULT_number_of_perception_nodes.append(len(tmp_animat_words))
		RESULT_word_occurenses[index] = RESULT_word_occurenses[index] + 1

		#Give the Animat a space between words
		t = t + 1
		test_environment.temporalState = " "
		test_animat.update(t,1)

		#update results
		tmp_animat_words = [n.getWord() for n in test_animat.network.perception_nodes]
		c = 0
		for w in words_to_use:
			if w in tmp_animat_words:
				c = c + 1
		RESULT_number_of_words_learnt.append(c)
		RESULT_number_of_perception_nodes.append(len(tmp_animat_words))
		RESULT_word_occurenses[index] = RESULT_word_occurenses[index] + 1
	#End for loop

	#Calculate final results
	RESULT_word_lengths = [len(s) for s in words_to_use]
	RESULT_animat_words = [n.getWord() for n in test_animat.network.perception_nodes] # All 'words' that the Animat has learnt.
	RESULT_learnt_words = [w for w in words_to_use if w in RESULT_animat_words]

	#Save results:
	file FileWriter("evaluationIO/" + "STEP:2 Results" + datetime.datetime.now().strftime("%y%m%d-%H%M%S") + ".m")
	file.writeLineToFile()

	file.writeLineToFile("% Results to save:")
	file.writeLineToFile("RESULT_number_of_words_learnt = " + RESULT_number_of_words_learnt)
	file.writeLineToFile("RESULT_number_of_perception_nodes = " + RESULT_number_of_perception_nodes)
	file.writeLineToFile("RESULT_word_occurenses = " + RESULT_word_occurenses)
	file.writeLineToFile("RESULT_word_lengths = " + RESULT_word_lengths)
	file.writeLineToFile("RESULT_animat_words = " + RESULT_animat_words)
	file.writeLineToFile("RESULT_learnt_words = " + RESULT_learnt_words)
	file.writeLineToFile("% Input to save:")
	file.writeLineToFile("TOTAL_NUMBER_OF_WORDS = " + TOTAL_NUMBER_OF_WORDS)
	file.writeLineToFile("AVERAGE_NUMBER_OF_OCCURENCES_OF_EACH_WORD = " + AVERAGE_NUMBER_OF_OCCURENCES_OF_EACH_WORD)
	file.writeLineToFile("SEQ_FORMATION_PROBABILITY = " + SEQ_FORMATION_PROBABILITY)
	file.writeLineToFile("% Absolute constatns to save:")
	file.writeLineToFile("TEMPORAL_MEMORY_CAPACITY = " + TEMPORAL_MEMORY_CAPACITY)
	file.writeLineToFile("SEQ_FORMATION_MAX_ATTEMPTS = " + SEQ_FORMATION_MAX_ATTEMPTS)



