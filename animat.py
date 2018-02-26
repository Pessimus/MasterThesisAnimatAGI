import numpy as np


class Animat:
	def __init__(self, name = None, sensors = [], motors = [], perception_nodes = [], action_nodes = [], memory_capacity = 0, temporal_memory_capacity = 0):
		#create network
		self.sensors = sensors
		self.motors = motors
		self.perception_nodes = perception_nodes
		self.action_nodes = action_nodes

		i = 0
		for node in sensors:
			node.index = i
			i = i + 1
		for node in perception_nodes:
			node.index = i
			i = i + 1
		
		i = 0
		for node in motors:
			node.index = i
			i = i + 1
		for node in action_nodes:
			node.index = i
			i = i + 1

		self.number_of_sensors = len(sensors)
		self.number_of_motors = len(motors)
		self.number_of_perception_nodes = len(perception_nodes)
		self.number_of_action_nodes = len(action_nodes)
		self.total_number_of_input_nodes = self.number_of_sensors + self.number_of_perception_nodes
		self.total_number_of_output_nodes = self.number_of_motors + self.number_of_action_nodes
		self.total_number_of_nodes = self.total_number_of_input_nodes + self.total_number_of_output_nodes

		#initialize short term memories
		self.memory_capacity = memory_capacity
		self.short_term_memory = []
		self.temporal_memory_capacity = memory_capacity
		self.temporal_short_term_memory = []


		#create matrices
		self.temporal_transition_matrix = np.zeros((self.total_number_of_input_nodes, self.total_number_of_output_nodes, self.total_number_of_input_nodes)) #probability of 3 becoming active if 2 was preformed when 1 was active.
		#self.sequence_matrix = np.zeros((total_number_of_input_nodes,total_number_of_input_nodes)) #might be added later...
		#self.temporal_sequence_matrix = np.zeros((self.total_number_of_input_nodes, self.total_number_of_input_nodes)) #Fraction over the last 100 ticks that 1 has been top active at t and 2 at (t-1)
		self.conditional_matrix = np.zeros((self.total_number_of_input_nodes, self.total_number_of_input_nodes)) #Intuition: Probability that 1 is top active at t given that 2 is top active at t: Pr(1|2)
		self.time_extended_conditional_matrix = np.zeros((self.total_number_of_input_nodes, self.total_number_of_input_nodes)) #Intuition: Probability that 1 is top active at ~t given that 2 is top active at t: Pr(1|2)
	#End __init__()

	#Adds a new perception node to the list of perseption nodes. And increases the size of all matrices to accomodate for the new node. 
	def add_perception_node(self, node):
		self.perception_nodes.append(node)
		node.index = self.total_number_of_input_nodes

		self.number_of_perception_nodes = self.number_of_perception_nodes + 1
		self.total_number_of_input_nodes = self.total_number_of_input_nodes + 1
		self.total_number_of_nodes = self.total_number_of_nodes + 1

		#update temporal_transition_matrix
		new_layer = np.zeros((1,self.total_number_of_output_nodes, self.total_number_of_input_nodes-1))
		self.temporal_transition_matrix = np.append(self.temporal_transition_matrix, new_layer, 0)
		new_column = np.zeros((self.total_number_of_input_nodes,self.total_number_of_output_nodes,1))
		self.temporal_transition_matrix = np.append(self.temporal_transition_matrix, new_column, 2)

		#update temporal_sequence_matrix
		self.temporal_sequence_matrix = np.append(self.temporal_sequence_matrix, zeros((1,self.total_number_of_input_nodes-1)), 0)
		self.temporal_sequence_matrix = np.append(self.temporal_sequence_matrix, zeros((self.total_number_of_input_nodes, 1)), 1)

		#update conditional_matrix
		self.conditional_matrix = np.append(self.conditional_matrix, zeros((1,self.total_number_of_input_nodes-1)), 0)
		self.conditional_matrix = np.append(self.conditional_matrix, zeros((self.total_number_of_input_nodes, 1)), 1)

		#update time_extended_conditional_matrix
		self.time_extended_conditional_matrix = np.append(self.time_extended_conditional_matrix, zeros((1,self.total_number_of_input_nodes-1)), 0)
		self.time_extended_conditional_matrix = np.append(self.time_extended_conditional_matrix, zeros((self.total_number_of_input_nodes, 1)), 1)

	#End add_perception_node()

	#Adds a new action node to the list of action nodes. And increases the size of matrices to accomodate for the new node. 
	def add_action_node(self,node):
		self.action_nodes.append(node)
		node.index = self.total_number_of_output_nodes

		self.number_of_action_nodes = self.number_of_action_nodes + 1
		self.total_number_of_output_nodes = self.total_number_of_output_nodes + 1
		self.total_number_of_nodes = self.total_number_of_nodes + 1

		#update temporal_transition_matrix
		new_layer = np.zeros((self.total_number_of_input_nodes, 1, self.total_number_of_input_nodes))
		self.temporal_transition_matrix = np.append(self.temporal_transition_matrix, new_layer, 1)
	#End add_action_node
#End Class Animat

