import numpy as np
import random
import bisect
from network import *


class Animat:
	def __init__(self, name = None, sensors = [], motors = [], perception_nodes = [], action_nodes = [], memory_capacity = 0, temporal_memory_capacity = 0, seq_formation_probability = 0, seq_formation_max_attempts = 0):
		self.name = name
		self.network = Network(sensors, motors, perception_nodes, action_nodes, memory_capacity, temporal_memory_capacity)
		self.last_action = -1
		self.seq_formation_probability = seq_formation_probability
		self.seq_formation_max_attempts = seq_formation_max_attempts

	#End __init__()

	def update(self, time, temporal_input_length = 0):

		if time > 1:
			self.learn()

		self.network.update_previous_active()

		for tt in range(0,temporal_input_length):
			self.temporal_update(time, tt)

		self.network.tick(time)
		self.update_experiences()

		#self.act(time)
	#End update()

	def temporal_update(self, time, temporal_time):
		#print("Doing temporal stuff!")
		self.network.temporal_tick(time, temporal_time)

		#Learn
		self.update_temporal_experiences()

	#End temporal_update()

	#
	def update_step_one_version(self, time):
		#handle temporal input somehow
		#possibly learn from temporal input
		
		#tick network
		self.network.update_previous_active()
		self.network.tick(time)
		self.update_experiences()

		#end learning (learn from consequences of previous action in previous time step)
		#make decision
		#self.make_decision()
		#act
		self.babble(time)
		#begin learning
	#End update()

	#Should handle all the Animats learning, i.e. adding and removing nodes in the network.
	def learn(self):
	#	print("Animat: learn")
		#Probabilistic learning (temporal)
		#if coin flip says learn, then add node to network
		r = np.random.rand()
		if r < self.seq_formation_probability:
			probabilities = self.network.get_cumulative_temporal_seq_matrix()
			if(probabilities[-1] == 0): #Animat has not any sequenses for the last 100 temporal time steps. 
				return
			success = False
			attempts = 0
			while attempts <= self.seq_formation_max_attempts and not success:
				attempts = attempts + 1
				r = np.random.random() * probabilities[-1]
				indices = bisect.bisect(probabilities, r)
				node2_index,node1_index = np.unravel_index(indices, self.network.temporal_sequence_matrix.shape)
				success = self.network.create_and_add_temporal_seq_node(node1_index, node2_index)
			#print("added node")

	#End learn

	def act(self, time):
		self.babble(time)
	#End act()

	def begin_learning(self):
		print("Not yet implemented")
	#End begin_learning()

	def end_learning(self):
		print("Not yet implemented")
	#End end_learning()

	def make_decision(self):
		print("Not yet implemented")
	#End make_decision()

	def babble(self, time):
		num_motors = self.network.number_of_motors
		random_motor_index = random.randint(0,num_motors-1)
		if self.network.activate_action_node(random_motor_index, time):
			self.last_action = random_motor_index
		else:
			self.last_action = -1
	#End babble()

	def update_experiences(self):
		if not self.last_action == -1:
			self.network.update_transition_matrix(self.last_action)
			self.network.update_generators()
	#End update_experiences()

	def update_temporal_experiences(self):
		self.network.update_temporal_sequence_matrix()



	#End babble()


#End Class Animat

