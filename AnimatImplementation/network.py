import numpy as np
import AnimatImplementation.nodes as node_types
import AnimatImplementation.temporalNodes as temporal_node_types
import AnimatImplementation.temporalActionNodes as temporal_action_node_types
from scipy import spatial
import bisect
import math

def safe_div(x,y):
	if y == 0:
		return 0
	return x/(y*1.0)

#Class reprecenting the network used by a Animat. Containing all nodes and the matrices for them.
class Network():
	def __init__(self, sensors = [], motors = [], perception_nodes = [], action_nodes = [], memory_capacity = 0, temporal_memory_capacity = 0):
		#create network
		true_node = node_types.SensorNode("True Node", "true", None) #All networks should have a 'true' node, that has index 0.
		self.sensors = [true_node] + sensors
		self.motors = motors
		self.perception_nodes = perception_nodes
		self.action_nodes = action_nodes

		i = 0
		for node in self.sensors:
			node.index = i
			i = i + 1
		for node in self.perception_nodes:
			node.index = i
			i = i + 1
		
		i = 0
		for node in self.motors:
			node.index = i
			i = i + 1
		for node in self.action_nodes:
			node.index = i
			i = i + 1

		self.number_of_sensors = len(self.sensors)
		self.number_of_motors = len(motors)
		self.number_of_perception_nodes = len(perception_nodes)
		self.number_of_action_nodes = len(action_nodes)
		self.total_number_of_input_nodes = self.number_of_sensors + self.number_of_perception_nodes
		self.total_number_of_output_nodes = self.number_of_motors + self.number_of_action_nodes
		self.total_number_of_nodes = self.total_number_of_input_nodes + self.total_number_of_output_nodes

		#initialize short term memories
		self.memory_capacity = memory_capacity
		self.short_term_memory = []
		self.temporal_memory_capacity = temporal_memory_capacity
		self.temporal_short_term_memory = []


		#create matrices
		#--transition_matrix--
		#probability of 3 becoming topactive if 2 was preformed when 1 was active.
		#axis 0 (layer) perception, axis 1 (row) action, axis 2 (column) perception
		#self.transition_matrix = np.zeros((self.total_number_of_input_nodes, self.total_number_of_output_nodes, self.total_number_of_input_nodes), dtype=(float,2))# OLD
		#self.transition_matrix = [([ [(0,0)] * self.total_number_of_input_nodes for _ in range(self.total_number_of_output_nodes) ]) for _ in range(self.total_number_of_input_nodes)]
		self.simple_transition_matrix = [([ [(0,0)] * self.total_number_of_input_nodes for _ in range(self.total_number_of_output_nodes) ]) for _ in range(1)]
		#self.sequence_matrix = np.zeros((total_number_of_input_nodes,total_number_of_input_nodes)) #might be added later...
		#self.temporal_sequence_matrix = np.zeros((self.total_number_of_input_nodes, self.total_number_of_input_nodes)) #Fraction over the last 100 ticks that 1 has been top active at t and 2 at (t-1)
		#self.temporal_sequence_matrix = np.zeros((self.total_number_of_input_nodes, self.total_number_of_input_nodes), dtype = object) #Fraction over the last 100 ticks that 1 has been top active at t and 2 at (t-1)
		#for i in range(0,self.temporal_sequence_matrix.shape[0]):
		#	for j in range(0,self.temporal_sequence_matrix.shape[1]):
		#		self.temporal_sequence_matrix[i][j] = []
		self.temporal_sequence_matrix = [ [0] * self.total_number_of_input_nodes for _ in range(self.total_number_of_input_nodes) ]
		for i in range(self.total_number_of_input_nodes):
			for j in range(self.total_number_of_input_nodes):
				self.temporal_sequence_matrix[i][j] = []


		#self.conditional_matrix = np.zeros((self.total_number_of_input_nodes, self.total_number_of_input_nodes)) #Intuition: Probability that 1 is top active at t given that 2 is top active at t: Pr(1|2)
		#self.conditional_matrix = [ [0] * self.total_number_of_input_nodes for _ in range(self.total_number_of_input_nodes) ] #dividends
		self.conditional_matrix_divisor = [0] * self.total_number_of_input_nodes #divisors

		#self.time_extended_conditional_matrix = np.zeros((self.total_number_of_input_nodes, self.total_number_of_input_nodes)) #Intuition: Probability that 1 is top active at ~t given that 2 is top active at t: Pr(1|2)
		self.time_extended_conditional_matrix = [ [0] * self.total_number_of_input_nodes for _ in range(self.total_number_of_input_nodes) ]


		#TODO: this shold be updated to work in a more general way.
		self.generator_list = np.ones((self.total_number_of_input_nodes), dtype=int)*(-1)

		self.input_nodes_names = [n.name for n in self.sensors+self.perception_nodes]
	#End __init__()

	#Adds a new perception node to the list of perseption nodes. And increases the size of all matrices to accomodate for the new node. 
	def add_perception_node(self, node):
		if node.name in self.input_nodes_names:
			return False

		self.perception_nodes.append(node)
		node.index = self.total_number_of_input_nodes

		self.number_of_perception_nodes = self.number_of_perception_nodes + 1
		self.total_number_of_input_nodes = self.total_number_of_input_nodes + 1
		self.total_number_of_nodes = self.total_number_of_nodes + 1

		#update transition_matrix
		#new_layer = np.zeros((1,self.total_number_of_output_nodes, self.total_number_of_input_nodes-1), dtype=(float,2))
		#self.transition_matrix = np.append(self.transition_matrix, new_layer, 0)
		#new_column = np.zeros((self.total_number_of_input_nodes,self.total_number_of_output_nodes,1), dtype=(float,2))
		#self.transition_matrix = np.append(self.transition_matrix, new_column, 2)
		#self.transition_matrix.append([ [(0,0)] * (self.total_number_of_input_nodes-1) for _ in range(self.total_number_of_output_nodes) ])
		#for x in self.transition_matrix:
		#	for y in x:
		#		y.append((0,0))
		for x in self.simple_transition_matrix:
			for y in x:
				y.append((0,0))


		#update temporal_sequence_matrix
		#v1 = np.zeros((1,self.total_number_of_input_nodes-1), dtype = object)
		#for i in range(0, v1.shape[1]):
		#	v1[0][i] = []
		#v2 = np.zeros((self.total_number_of_input_nodes, 1), dtype = object)
		#for i in range(0, v2.shape[0]):
		#	v2[i][0] = []
		#self.temporal_sequence_matrix = np.append(self.temporal_sequence_matrix, v1, 0)
		#self.temporal_sequence_matrix = np.append(self.temporal_sequence_matrix, v2, 1)
		self.temporal_sequence_matrix.append([ [] * (self.total_number_of_input_nodes-1) for _ in range((self.total_number_of_input_nodes-1)) ])
		for i in self.temporal_sequence_matrix:
			i.append([])


		#update conditional_matrix
		#self.conditional_matrix = np.append(self.conditional_matrix, np.zeros((1,self.total_number_of_input_nodes-1)), 0)
		#self.conditional_matrix = np.append(self.conditional_matrix, np.zeros((self.total_number_of_input_nodes, 1)), 1)
		#self.conditional_matrix.append( [0] * (self.total_number_of_input_nodes-1)) #add another list with zeros
		#for i in self.conditional_matrix:
		#	i.append(0) #in each list, add a zero
		self.conditional_matrix_divisor.append(0)
		#update time_extended_conditional_matrix
		#self.time_extended_conditional_matrix = np.append(self.time_extended_conditional_matrix, np.zeros((1,self.total_number_of_input_nodes-1)), 0)
		#self.time_extended_conditional_matrix = np.append(self.time_extended_conditional_matrix, np.zeros((self.total_number_of_input_nodes, 1)), 1)
		#self.time_extended_conditional_matrix.append([ [] * (self.total_number_of_input_nodes-1) for _ in range((self.total_number_of_input_nodes-1)) ]) #TODO: probably broken
		self.time_extended_conditional_matrix.append([0] * (self.total_number_of_input_nodes-1))
		for i in self.time_extended_conditional_matrix:
			i.append(0)

		self.input_nodes_names.append(node.name)

		self.generator_list = np.append(self.generator_list, -1)

		return True
	#End add_perception_node()

	#Adds a new action node to the list of action nodes. And increases the size of matrices to accomodate for the new node. 
	def add_action_node(self,node):
		self.action_nodes.append(node)
		node.index = self.total_number_of_output_nodes

		self.number_of_action_nodes = self.number_of_action_nodes + 1
		self.total_number_of_output_nodes = self.total_number_of_output_nodes + 1
		self.total_number_of_nodes = self.total_number_of_nodes + 1

		#update transition_matrix
		#new_layer = np.zeros((self.total_number_of_input_nodes, 1, self.total_number_of_input_nodes), dtype=(float,2))#OLD
		#self.transition_matrix = np.append(self.transition_matrix, new_layer, 1)

		for x in self.simple_transition_matrix:
			x.append([(0,0)] * self.total_number_of_input_nodes)

	#End add_action_node

	#Removes a preception node from the graph and all matrices, iff the node is a top node.
	#DEPRICATED after change of data srtucture for transition_matrix
	#def remove_perception_node(self, node):
	#	if self.is_top_perception_node(node):
	#		index = node.get_index()
	#		list_position = index - self.number_of_sensors
	#
	#		for n in self.perception_nodes:
	#			if n.get_index() > index:
	#				n.index = n.index - 1
	#
	#		del self.perception_nodes[list_position]
	#
	#		self.transition_matrix = np.delete(self.transition_matrix, index, 0)
	#		self.transition_matrix = np.delete(self.transition_matrix, index, 2)
	#
	#		self.temporal_sequence_matrix = np.delete(self.temporal_sequence_matrix, index, 0)
	#		self.temporal_sequence_matrix = np.delete(self.temporal_sequence_matrix, index, 1)
	#		
	#		self.conditional_matrix = np.delete(self.conditional_matrix, index, 0)
	#		self.conditional_matrix = np.delete(self.conditional_matrix, index, 1)
	#
	#		self.time_extended_conditional_matrix = np.delete(self.time_extended_conditional_matrix, index, 0)
	#		self.time_extended_conditional_matrix = np.delete(self.time_extended_conditional_matrix, index, 1)
	#
	#		self.number_of_perception_nodes=self.number_of_perception_nodes-1
	#		self.total_number_of_input_nodes=self.total_number_of_input_nodes-1
	#		self.total_number_of_nodes=self.total_number_of_nodes-1
	#
	#		return True
	#	else:
	#		return False
	#End remove_perception_node()

	# Returns true if the node is not input to any other node.
	def is_top_perception_node(self, node):
		for n in self.perception_nodes:
			if node in n.inputs:
				return False
		return True
	#End is_top_perception_node()

	#Removes a action node from the graph and all matrices, iff the node is a top node.
	#DEPRICATED after change of data srtucture for transition_matrix
	#def remove_action_node(self,node):
	#	if self.is_top_action_node(node):
	#		index = node.get_index()
	#		list_position = index - self.number_of_motors
	#
	#		for n in self.action_nodes:
	#			if n.get_index() > index:
	#				n.index = n.index - 1
	#
	#		del self.action_nodes[list_position]
	#
	#		self.transition_matrix = np.delete(self.transition_matrix, index, 1)
	#
	#		self.number_of_action_nodes = self.number_of_action_nodes - 1
	#		self.total_number_of_output_nodes = self.total_number_of_output_nodes - 1
	#		self.total_number_of_nodes = self.total_number_of_nodes - 1
	#
	#		return True
	#	else:
	#		return False
	#End remove_action_node()

	# Returns true if the node is not input to any other node.
	def is_top_action_node(self, node):
		for n in self.action_nodes:
			if node in n.outputs:
				return False
		return True
	#End is_top_action_node()

	#For all nodes, set previous active to the current value of active. 
	def update_previous_active(self):
		for node in self.sensors:
			node.previous_active = node.active
		for node in self.perception_nodes:
			node.previous_active = node.active
	#Endupdate_previous_active()

	#For all nodes, sets the value of active to false.
	def deactivate_all_nodes(self):
		for node in self.sensors:
			node.active = False
		for node in self.perception_nodes:
			node.active = False
	#End deactivate_all_nodes()

	#Returns a list of all topactive nodes in the network.
	def get_topactive_nodes(self):
		#Start by setting al nodes as topactive, so that the ones that are not can be deactivated.
		for node in self.sensors:
			node.topactive = True
		for node in self.perception_nodes:
			node.topactive = True

		#Set all nodes that should not be topactive as not topactive (they also do this to all their input). 
		for node in self.sensors:
			node.update_topactive(self)
		for node in self.perception_nodes:
			node.update_topactive(self)

		#Get the list to return.
		result = []
		for node in self.sensors:
			if node.topactive:
				result.append(node)
		for node in self.perception_nodes:
			if node.topactive:
				result.append(node)

		return result
	#End get_topactive_nodes()

	#Ticks all the sensor and perseption nodes in the network.  
	def tick(self, time):
		for node in self.sensors:
			node.tick(time)
		for node in self.perception_nodes:
			node.tick(time)

		#update short term memory
		topactive_nodes = self.get_topactive_nodes()
		self.short_term_memory.insert(0,topactive_nodes)
		if(len(self.short_term_memory) > self.memory_capacity):
			self.short_term_memory.pop()
	#End tick()

	#Ticks all the sensor and perseption nodes in the network with a temporal tick.  
	def temporal_tick(self, time, temporal_time):
		#tick all nodes in the network
		for node in self.sensors:
			node.tick(time, temporal_time, True)
		for node in self.perception_nodes:
			node.tick(time, temporal_time, True)
		#update temporal short term memory
		topactive_nodes = self.get_topactive_nodes()
		self.temporal_short_term_memory.insert(0,topactive_nodes)
		if(len(self.temporal_short_term_memory) > self.temporal_memory_capacity):
			self.temporal_short_term_memory.pop()
	#End temporal_tick()

	#Method for debugging, returns all the 'words' reprecented by the nodes in the network.
	def print_network(self):
		print("----Printing Network----")
		print("Printing sensors:")
		for node in self.sensors:
			print("\t" + "Word:" + str(node.get_word()))
			print("\t" + "Active:" + str(node.is_active()))
			print("\t" + "Was Active:" + str(node.was_active()))
			print("\t" + "Was temporal Active:" + str(node.was_temporal_active()))
			print("")
		print("Printing perception nodes:")
		for node in self.perception_nodes:
			print("\t" + "Word:" + str(node.get_word()))
			print("\t" + "Active:" + str(node.is_active()))
			print("\t" + "Was Active:" + str(node.was_active()))
			print("\t" + "Was temporal Active:" + str(node.was_temporal_active()))
			print("")
		print("Printing motor nodes:")
		for node in self.motors:
			print("\t" + "Word:" + str(node.get_word()))
			print("")
		print("Printing action nodes:")
		for node in self.action_nodes:
			print("\t" + "Word:" + str(node.get_word()))
			print("")
	#End print_network()

	#Returns the action node with the given index if such a node exists
	def get_action_node(self, index):
		if index < self.number_of_motors:
			return self.motors[index]
		elif (index-self.number_of_motors) < self.number_of_action_nodes:
			return self.action_nodes[index-self.number_of_motors]
		else:
			return None
	#End get_action_node()


	#Returns the perception node with the given index if such a node exists
	def get_perception_node(self, index):
		if index < self.number_of_sensors:
			return self.sensors[index]
		elif (index-self.number_of_sensors) < self.number_of_perception_nodes:
			return self.perception_nodes[index-self.number_of_sensors]
		else:
			return None
	#End get_perception_node()

	def activate_action_node(self, index, time, temporal = False):
		if index < self.number_of_motors:
			return self.motors[index].activate(time, temporal)
		elif (index-self.number_of_sensors) < self.number_of_action_nodes:
			return self.action_nodes[index-self.number_of_motors].activate(time, temporal)
		else:
			return False
	#End activate_action_node()

	def update_temporal_sequence_matrix(self):
		#Update all tick counters.
		#for i in range(0,self.temporal_sequence_matrix.shape[0]):
		for i in range(0,len(self.temporal_sequence_matrix)):
			#for j in range(0,self.temporal_sequence_matrix.shape[1]):
			for j in range(0,len(self.temporal_sequence_matrix[0])):
				v = self.temporal_sequence_matrix[i][j]
				#if not v == 0:
				v2 =  []
				for e in v:
					if e < 100:
						v2.append(e+1)
					#end if
				#end if
				self.temporal_sequence_matrix[i][j] = v2

		#Add new tick counters.
		topactive_nodes = self.get_topactive_nodes()

		#TODO: TESTING NEW FIX
		#activation_times = [n.activation_time() for n in topactive_nodes]
		#min_at = min(activation_times)
		#if min_at >= len(self.temporal_short_term_memory):
		#	nodes_to_use = self.sensors
		#	print("this")
		#else:
		#	nodes_to_use = topactive_nodes
		#for node in nodes_to_use:
		
		for node in topactive_nodes:
			activation_time = node.activation_time()
			if len(self.temporal_short_term_memory) > activation_time:
				previous_top_actives = self.temporal_short_term_memory[activation_time]
				for node_prime in previous_top_actives:
					node_index = node.get_index()
					node_prime_index = node_prime.get_index()
					(self.temporal_sequence_matrix[node_index][node_prime_index]).append(1)
					#end else
	#End update_temporal_sequence_matrix()

	#Updates the values of the transition matrix, depending on what nodes were active, and what nodes are topactive.
	#Assumes that last_action is a valid action.
	#def update_transition_matrix(self, last_action):
	#	#probability of 3 becoming topactive if 2 was preformed when 1 was active.
	#	topactive_nodes = self.get_topactive_nodes()
	#	input_nodes = self.sensors + self.perception_nodes
	#	for last_state_node in input_nodes:
	#		if last_state_node.was_active():
	#			i = last_state_node.get_index()
	#			for current_state_node in input_nodes:
	#				j = current_state_node.get_index()
	#				dividend, divisor = self.transition_matrix[i][last_action][j]
	#				divisor = divisor + 1
	#				if current_state_node in topactive_nodes:
	#					dividend = dividend + 1
	#				self.transition_matrix[i][last_action][j] = (dividend, divisor)
	#End update_transition_matrix()

	#Updates the values of the transition matrix, depending on what nodes were active, and what nodes are topactive.
	#Simple version using only the true node as the previous node.
	#Assumes that last_action is a valid action.
	def update_transition_matrix(self, last_action):
		#probability of 3 becoming topactive if 2 was preformed when 1 was active.
		topactive_nodes = self.get_topactive_nodes()
		input_nodes = self.sensors + self.perception_nodes
		#for last_state_node in input_nodes:
		#	if last_state_node.was_active():
		#		i = last_state_node.get_index()
		i = 0 #Index of true node
		for current_state_node in input_nodes:
			j = current_state_node.get_index()
			dividend, divisor = self.simple_transition_matrix[i][last_action][j]
			divisor = divisor + 1
			if current_state_node in topactive_nodes:
				dividend = dividend + 1
			self.simple_transition_matrix[i][last_action][j] = (dividend, divisor)
	#End update_transition_matrix()

	#Updates a list of generators for all perception nodes. TODO: should be more general.
	def update_generators(self):
		input_nodes = self.sensors + self.perception_nodes
		output_nodes = self.motors + self.action_nodes
		for node in input_nodes:
			b = node.get_index()
			#self.generator_list[b] = -1
			if not self.generator_list[b] == -1:
				dividend, divisor = self.simple_transition_matrix[0][self.generator_list[b]][b]
				if not dividend == divisor:
					self.generator_list[b] = -1 # This was NOT a generator, as this has now been proven false (if divisor is 0 it has not been attempted, and can thus still be true.)

			for action in output_nodes: # Might not be needed depending on if-statement above, but could be used to find more than one generator.
				a = action.get_index()
				dividend, divisor = self.simple_transition_matrix[0][a][b]
				if divisor == dividend and not divisor == 0: #If the probability is one (not true if divisor is 0)
					self.generator_list[b] = a
	#End update_generators()

	def update_conditional_matrices(self):
		top_active_nodes = self.get_topactive_nodes()
		for first_node in top_active_nodes:
			first_node_index = first_node.get_index()

			#update conditional matrix
			#for second_node in top_active_nodes:
			#	second_node_index = second_node.get_index()
			#	dividend = self.conditional_matrix[first_node_index][second_node_index]
			#	self.conditional_matrix[first_node_index][second_node_index] = dividend + 1
			

			#update time-extended conditional matrix
			for previous_top_actives in (self.short_term_memory[1:]):
				for second_node in previous_top_actives:
					second_node_index = second_node.get_index()
					dividend = self.time_extended_conditional_matrix[first_node_index][second_node_index]
					#print("Debug")
					#print(dividend)
					self.time_extended_conditional_matrix[first_node_index][second_node_index] = dividend + 1
					dividend = self.time_extended_conditional_matrix[second_node_index][first_node_index]
					self.time_extended_conditional_matrix[second_node_index][first_node_index] = dividend + 1

			#count total nbr of occurences of this node
			divisor = self.conditional_matrix_divisor[first_node_index]
			self.conditional_matrix_divisor[first_node_index] = divisor + 1
	#End update_conditional_matrices()

	def get_cumulative_temporal_seq_matrix(self):
		#x,y = self.temporal_sequence_matrix.shape
		x = len(self.temporal_sequence_matrix)
		y = len(self.temporal_sequence_matrix[0])
		#temp_mat = np.zeros((x,y))
		#temp_mat = [ [0] * x for _ in range(y) ]
		try:
			temp_mat = [0] *(x*y)
		except MemoryError:
			print("x: = ")
			print(x)
			print("y: = ")
			print(y)

		#loop from 1 to avoid True node which is at index 1
		last_value = 0
		for i in range(1,x):
			for j in range(1,y):
				v = self.temporal_sequence_matrix[i][j]
				last_value = last_value + len(v)
				temp_mat[(i*y)+j] = last_value

		return temp_mat
		#return np.cumsum(temp_mat)
	#End get_cumulative_temporal_seq_matrix()

	def create_and_add_temporal_seq_node(self, input1, input2, should_add_action_node = False):
		input_nodes = self.sensors + self.perception_nodes
		node = temporal_node_types.TemporalSEQNode(inputs=[input_nodes[input1],input_nodes[input2]])
		success_perception = self.add_perception_node(node)

		if success_perception and should_add_action_node:
				output_nodes = self.motors + self.action_nodes
				a_input_1 = self.generator_list[input1]
				a_input_2 = self.generator_list[input2]
				action_node = temporal_action_node_types.TemporalASEQNode(outputs = [output_nodes[a_input_1], output_nodes[a_input_2]])
				self.add_action_node(action_node)
				self.generator_list[node.index] = action_node.index
		return success_perception
	#End create_and_add_temporal_seq_node()

	def associate(self, node_index):
		result_indices = []
		result_values = []
		simple = []

		#vector_to_compare = self.time_extended_conditional_matrix[node_index]
		vector_to_compare = [safe_div(x,y) for x, y in zip(self.time_extended_conditional_matrix[node_index][1:], self.conditional_matrix_divisor[1:])]
		#vector_to_compare = map(truediv, self.time_extended_conditional_matrix[node_index], self.conditional_matrix_divisor)


		if(sum(vector_to_compare) == 0):
			return [],[]

		for i in range(1,len(self.time_extended_conditional_matrix)):
			if(not i == node_index):
				#tmp_vector = self.time_extended_conditional_matrix[i]
				tmp_vector = [safe_div(x,y) for x, y in zip(self.time_extended_conditional_matrix[i][1:], self.conditional_matrix_divisor[1:])]
				#tmp_vector = map(truediv, self.time_extended_conditional_matrix[i], self.conditional_matrix_divisor)

				if(not sum(tmp_vector) == 0):
					tmp_res = spatial.distance.cosine(vector_to_compare,tmp_vector)

					insertion_point = bisect.bisect(result_values,tmp_res)

					result_values.insert(insertion_point, tmp_res)
					result_indices.insert(insertion_point, i)

					simple.append(tmp_res)
			else:
				simple.append(-1)

		#print(simple)

		#print(result_values)[0:10]
		#print(result_indices)[0:10]
		return result_values[0:10], result_indices[0:10]
	#End associate()

	def associate_action(self, node_index, number_of_associations):

		result_indices = []
		result_values = []

		#vector_to_compare = self.time_extended_conditional_matrix[node_index]
		vector_to_compare = [safe_div(x,y) for x, y in zip(self.time_extended_conditional_matrix[node_index][1:], self.conditional_matrix_divisor[1:])]
		#vector_to_compare = map(truediv, self.time_extended_conditional_matrix[node_index], self.conditional_matrix_divisor)

		if(sum(vector_to_compare) == 0):
			return [],[]

		for i in range(1,len(self.time_extended_conditional_matrix)):
			if(not i == node_index):
				#tmp_vector = self.time_extended_conditional_matrix[i]
				tmp_vector = [safe_div(x,y) for x, y in zip(self.time_extended_conditional_matrix[i][1:], self.conditional_matrix_divisor[1:])]
				#tmp_vector = map(truediv, self.time_extended_conditional_matrix[i], self.conditional_matrix_divisor)

				if(not sum(tmp_vector) == 0):
					tmp_res = spatial.distance.cosine(vector_to_compare,tmp_vector)

					insertion_point = bisect.bisect(result_values,tmp_res)

					result_values.insert(insertion_point, tmp_res)
					result_indices.insert(insertion_point, i)

		return_values = []
		return_indices = []

		i = 0
		for node_index in result_indices:
			generator = self.generator_list[node_index]
			if not generator == -1:
				return_indices.append(generator)
				return_values.append(result_values[i])
			if(len(return_indices) == number_of_associations):
				break

			i = i + 1

		#print(return_indices)

		return return_values, return_indices

	def associate_non_action(self, node_index, number_of_associations):

		result_indices = []
		result_values = []

		#vector_to_compare = self.time_extended_conditional_matrix[node_index]
		vector_to_compare = [safe_div(x,y) for x, y in zip(self.time_extended_conditional_matrix[node_index][1:], self.conditional_matrix_divisor[1:])]
		#vector_to_compare = map(truediv, self.time_extended_conditional_matrix[node_index], self.conditional_matrix_divisor)

		if(sum(vector_to_compare) == 0):
			return [],[]

		for i in range(1,len(self.time_extended_conditional_matrix)):
			if(not i == node_index):
				#tmp_vector = self.time_extended_conditional_matrix[i]
				tmp_vector = [safe_div(x,y) for x, y in zip(self.time_extended_conditional_matrix[i][1:], self.conditional_matrix_divisor[1:])]
				#tmp_vector = map(truediv, self.time_extended_conditional_matrix[i], self.conditional_matrix_divisor)

				if(not sum(tmp_vector) == 0):
					tmp_res = spatial.distance.cosine(vector_to_compare,tmp_vector)

					insertion_point = bisect.bisect(result_values,tmp_res)

					result_values.insert(insertion_point, tmp_res)
					result_indices.insert(insertion_point, i)

		return_values = []
		return_indices = []

		i = 0
		for node_index in result_indices:
			generator = self.generator_list[node_index]
			if generator == -1:
				return_indices.append(node_index)
				return_values.append(result_values[i])
			if(len(return_indices) == number_of_associations):
				break

			i = i + 1

		#print(return_indices)

		return return_values, return_indices

#End class



