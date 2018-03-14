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
	#Define constatns
	NUMBER_OF_OCCURENCES_OF_WORDS = 4*50
	TEMPORAL_MEMORY_CAPACITY = 5
	SEQ_FORMATION_PROBABILITY = 1/float(25)
	SEQ_FORMATION_MAX_ATTEMPTS = 10
	INPUT_FILE_NAME = "evaluationIO/animal_words.txt"

	#Create the Animat
	test_environment = Environment()	
	sensors, motors = create_nodes_for_alphabet(test_environment)

	totlal_number_of_sensors = len(sensors)
	test_animat = Animat("TheCat", sensors, motors, temporal_memory_capacity = TEMPORAL_MEMORY_CAPACITY, seq_formation_probability = SEQ_FORMATION_PROBABILITY, seq_formation_max_attempts = SEQ_FORMATION_MAX_ATTEMPTS)

	#Create arrays for words to input to the animate
	input_file = FileReader(INPUT_FILE_NAME)
	all_words = input_file.get_entire_file_as_array()
	all_words = all_words[0:10]
	number_of_words = len(all_words)

	word_indices = np.array([])
	for i in range(0, number_of_words):
		tmp_array = np.ones((NUMBER_OF_OCCURENCES_OF_WORDS))*i
		word_indices = np.concatenate((word_indices, tmp_array))

	shuffle(word_indices)

	#Train the Animat
	t = 0
	for index in word_indices:
		t = t + 1
		if t == 500 or t == 1000 or t == 1500 or t == 2000:
			print("TIME IS NOW: %d"%(t))

		#update environment
		word = all_words[int(index)]
		test_environment.temporalState = word

		#Update the Animat
		test_animat.update(t,len(word))
	#End for loop

	#Get results


	#mat = np.zeros(test_animat.network.temporal_sequence_matrix.shape)
	#for i in range(0,test_animat.network.temporal_sequence_matrix.shape[0]):
	#	for j in range(0,test_animat.network.temporal_sequence_matrix.shape[1]):
	#		v = test_animat.network.temporal_sequence_matrix[i][j]
	#		if not v == 0:
	#			mat[i][j] = len(v)
	#print("\nSimpler form:")
	#print(mat)

	#print("perception nodes: ")
	print("Printing ALL perception nodes in the Animat (not sensors)")
	animat_words = [n.getWord() for n in test_animat.network.perception_nodes]
	print(animat_words)

	c = 0
	for w in all_words:
		if w in animat_words:
			c = c + 1
	print("\nThe Animat has learnt %d of %d words.\n" % (c,number_of_words))

	print(all_words)




	#mat = np.zeros(test_animat.network.temporal_sequence_matrix.shape)
	lens = []
	nbr_ok_values = 0
	nbr_not_ok_values = 0
	for i in range(0,test_animat.network.temporal_sequence_matrix.shape[0]):
		for j in range(0,test_animat.network.temporal_sequence_matrix.shape[1]):
			v = test_animat.network.temporal_sequence_matrix[i][j]
			if not v == 0:
				lens.append(len(v))
				for e in v:
					if e <= 100:
						nbr_ok_values = nbr_ok_values + 1
					else:
						nbr_not_ok_values = nbr_not_ok_values + 1
	#print(lens)
	sum = 0
	for s in lens:
		sum = sum + s
	print("Sum of lenghts is %d"%(sum))
	print("Number of ok values in matrix is %d"%(nbr_ok_values))









