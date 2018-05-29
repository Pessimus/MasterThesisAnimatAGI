import numpy as np
import random
import bisect
from Chunking_Animat.network import *
from scipy import spatial


class Animat:
	def __init__(self, name = None, sensors = [], motors = [], perception_nodes = [], action_nodes = [], memory_capacity = 0, seq_formation_probability = 0, seq_formation_max_attempts = 0, learn_to_associate = False):
		self.name = name
		self.network = Network(sensors, motors, perception_nodes, action_nodes, memory_capacity)
		self.last_action = -1
		self.seq_formation_probability = seq_formation_probability
		self.seq_formation_max_attempts = seq_formation_max_attempts
		self.time = 0
		self.learn_to_associate = learn_to_associate
		#self.babbling = False

	#End __init__()

	def update(self, time, babble = False):
		if(self.time < time):
			self.time = time
			#self.babbling = babble
			
			if not babble and time > 1:
				self.learn(False)
			
			self.network.update_previous_active()

			self.network.tick(time)
			if not babble:
				self.network.update_sequence_matrix()

			self.update_experiences()

			self.last_action = -1
			if babble:
				self.babble(time)
		#end if(self.time < time)
	#End update()

	def repeat(self, time, temporal_input_length = 0, speak = True):
		self.network.update_previous_active()
		
		for tt in range(0,temporal_input_length):
			self.temporal_update(time, tt)

		self.network.tick(time)

		top_actives = self.network.get_topactive_nodes()
		actions = self.network.motors + self.network.action_nodes

		max_sequence_length = 0
		generator = -1

		if speak:
			if not len(top_actives) == 1: # A word is recognised
				for i in range(1,len(top_actives)):
					n = top_actives[i]
					#print(":::"+n.get_word())
					g = self.network.generator_list[n.index]
					if not g == -1:
						if n.activation_time() > max_sequence_length:
							max_sequence_length = n.activation_time()
							generator = g
				if not generator == -1:
					self.network.activate_action_node(generator, time, True)

	#End repeat

	def associate_action(self, number_of_associations):
		nodes = self.network.motors + self.network.action_nodes

		top_active_nodes_now = self.network.get_topactive_nodes()

		most_specific_so_far = -1
		max_sequence_length = 0
		for node in top_active_nodes_now:
			if(node.activation_time() > max_sequence_length and not node.get_word() == "true"):
				max_sequence_length = node.activation_time()
				most_specific_so_far = node.get_index()

		association_values, associated_nodes = self.network.associate_action(most_specific_so_far,number_of_associations)

		#association_values, associated_nodes = self.network.associate(1)

		return_list = [nodes[n].get_word() for n in associated_nodes]

		return return_list
		
	#End associate()

	def associate(self):
		nodes = self.network.sensors + self.network.perception_nodes

		top_active_nodes_now = self.network.get_topactive_nodes()

		most_specific_so_far = -1
		max_sequence_length = 0
		for node in top_active_nodes_now:
			if(node.activation_time() > max_sequence_length and not node.get_word() == "true"):
				max_sequence_length = node.activation_time()
				most_specific_so_far = node.get_index()

	#	print(nodes[most_specific_so_far].get_word())

		association_values, associated_nodes = self.network.associate(most_specific_so_far)
		#association_values, associated_nodes = self.network.associate(1)

		return_list = [nodes[n].get_word() for n in associated_nodes]

		return return_list
		
	#End associate()

	#Should handle all the Animats learning, i.e. adding and removing nodes in the network.
	def learn(self, probabilistic_add_action = False):
		#if coin flip says learn, then add node to network
		r = np.random.rand()
		if r < self.seq_formation_probability:
			probabilities = self.network.get_cumulative_seq_matrix()
			if(probabilities[-1] == 0): #Animat has not any sequenses for the last 100 time steps. 
				return
			success = False
			attempts = 0
			while attempts <= self.seq_formation_max_attempts and not success:
				attempts = attempts + 1
				r = np.random.random() * probabilities[-1]
				indices = bisect.bisect(probabilities, r)
				node2_index,node1_index = np.unravel_index(indices, (len(self.network.sequence_matrix),len(self.network.sequence_matrix[0])))

				inputnodes = self.network.sensors + self.network.perception_nodes

				success = self.network.create_and_add_seq_node(node1_index, node2_index, probabilistic_add_action)

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
		if self.learn_to_associate:
			self.network.update_conditional_matrices()
		#if not self.babbling:
		#	self.network.update_sequence_matrix()
	#End update_experiences()


#End Class Animat

